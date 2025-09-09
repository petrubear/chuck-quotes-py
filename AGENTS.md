# Project Architecture Overview for Agents

This document provides a technical overview of the project's architecture, intended for AI agents and developers who need to understand the system's components and their interactions.

## Architecture: Hexagonal (Ports and Adapters)

The application follows a strict Hexagonal Architecture, which separates the core business logic from external concerns. This design promotes modularity, testability, and maintainability.

### Core Component: `domain`

- **Location**: `/domain`
- **Purpose**: Contains the heart of the application. It is completely self-contained and has no dependencies on any other layer.
- **Key Components**:
    - `model/quote.py`: The central domain entity, `Quote`, is a simple dataclass.
    - `ports/inbound/get_quote_port.py`: An abstract base class (`GetQuotePort`) defining the primary entry point for application functionality (what the application can do).
    - `ports/outbound/retrieve_quote_port.py`: An abstract base class (`RetrieveQuotePort`) defining the interface for a secondary actor that provides data to the application (what the application needs from the outside world).

### Orchestration Component: `application`

- **Location**: `/application`
- **Purpose**: This layer orchestrates the flow of data and implements the business rules defined by the use cases.
- **Key Components**:
    - `usecases/get_quote_usecase.py`: The `GetQuoteUseCase` class implements the `GetQuotePort` (inbound port). It depends on the `RetrieveQuotePort` (outbound port) interface to fetch data, decoupling it from the specific implementation of the data source.
    - `service/quote_service.py`: A service that encapsulates the use case. In this project, it's a simple pass-through, but in more complex applications, it could coordinate multiple use cases.

### External-Facing Component: `infrastructure`

- **Location**: `/infrastructure`
- **Purpose**: This layer handles all interactions with the outside world, including web frameworks, databases, and external APIs. It contains the concrete implementations of the ports defined in the `domain` layer.
- **Key Components**:
    - `controller/quote_controller.py`: An **inbound adapter** (or driving adapter). It uses FastAPI to expose an HTTP endpoint. It depends on the `application` layer to execute the use case and then maps the result to an HTTP response model (`QuoteResponse`).
    - `adapter/retrieve_quote_adapter.py`: An **outbound adapter** (or driven adapter). The `RetrieveQuoteAdapter` class implements the `RetrieveQuotePort` interface. It is responsible for making HTTP calls to the external Chuck Norris API using `httpx`. It also handles the transformation of the external API's data model (`ChuckQuote`) into the application's domain model (`Quote`).
    - `configuration/dependencies.py`: This file is crucial for wiring the architecture together. It uses FastAPI's dependency injection system to provide the concrete implementations of the ports to the application layer. For example, it injects `RetrieveQuoteAdapter` wherever `RetrieveQuotePort` is required.
    - `main.py`: The application's entry point. It initializes the FastAPI application and manages application-level resources, such as the `httpx.AsyncClient` instance.

## Data Flow Example: `GET /api/v1/quote`

1.  An HTTP GET request hits the `get_quote` endpoint in `infrastructure/controller/quote_controller.py`.
2.  FastAPI's dependency injection system resolves the `quote_service` dependency.
3.  To create `QuoteService`, it needs a `GetQuoteUseCase`. To create `GetQuoteUseCase`, it needs a `RetrieveQuotePort`.
4.  The DI system provides the `RetrieveQuoteAdapter` as the concrete implementation for `RetrieveQuotePort`.
5.  The controller calls `quote_service.get_quote()`.
6.  The service calls `get_quote_usecase.get_quote()`.
7.  The use case calls `retrieve_quote_port.get_quote()`.
8.  This call executes the `get_quote` method on the `RetrieveQuoteAdapter`, which makes an HTTP request to the external API.
9.  The adapter receives the response, transforms it into a `Quote` domain object, and returns it.
10. The `Quote` object is passed back up to the controller.
11. The controller maps the `Quote` object to a `QuoteResponse` JSON object and returns it to the client.
