# Chuck Norris Quote API

This project is a simple API that provides Chuck Norris quotes, built using Python and FastAPI. It is designed following the principles of Hexagonal Architecture (also known as Ports and Adapters) to ensure a clean, maintainable, and testable codebase.

## Hexagonal Architecture

The project is divided into three main layers: `domain`, `application`, and `infrastructure`.

### 1. Domain Layer

This is the core of the application and contains the business logic and models. It is completely independent of any external frameworks or technologies.

- **`domain/model`**: Contains the domain models (e.g., `Quote`).
- **`domain/ports`**: Defines the interfaces (ports) for communication with the outside world.
  - **`inbound`**: Ports for driving the application (e.g., `GetQuotePort`).
  - **`outbound`**: Ports for secondary actors like databases or external APIs (e.g., `RetrieveQuotePort`).
- **`domain/exceptions`**: Custom exceptions for the domain.

### 2. Application Layer

This layer orchestrates the use cases of the application. It implements the inbound ports defined in the domain layer and uses the outbound ports.

- **`application/usecases`**: Contains the use case implementations (e.g., `GetQuoteUseCase`).
- **`application/service`**: Services that can coordinate multiple use cases (though in this simple project, it's a thin wrapper around a single use case).

### 3. Infrastructure Layer

This layer contains all the technology-specific implementations, such as API controllers, database adapters, and external API clients. It implements the outbound ports and drives the inbound ports.

- **`infrastructure/adapter`**: Contains the adapters that implement the outbound ports (e.g., `RetrieveQuoteAdapter` for fetching quotes from an external API).
- **`infrastructure/controller`**: Contains the API controllers (e.g., `quote_controller.py` using FastAPI) which act as inbound adapters.
- **`infrastructure/configuration`**: Handles dependency injection and configuration management.
- **`infrastructure/model`**: Contains data transfer objects (DTOs) for the infrastructure layer (e.g., `ChuckQuote`, `QuoteResponse`).

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd chuck-quotes
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** from the `.env.example` (if provided) or create a new one with the following content:
    ```
    CHUCK_API_URL=https://api.chucknorris.io/jokes/random
    ```

5.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **`GET /api/v1/quote`**: Retrieves a random Chuck Norris quote.
