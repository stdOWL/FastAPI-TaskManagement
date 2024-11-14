
# Task Management API

A FastAPI-based Task Management API for creating, updating, retrieving, and deleting tasks. This API supports PostgreSQL for database management.

## Project Structure

```
FastAPI-TaskManagement-DM/
├── app/
│   ├── core/                 # Core business logic
│   ├── cruds/                # Database operations
│   ├── enums/                # Enums for exceptions
│   ├── models/               # Database models
│   ├── routers/              # API routes
│   ├── schemas/              # Pydantic schemas
│   ├── dependencies.py       # Dependency management
│   └── database.py           # Database connection setup
├── tests/                    # Test cases
├── pyproject.toml            # Poetry dependencies and configuration
└── README.md                 # Project documentation
```

## Prerequisites

1. **Poetry**: For dependency management and virtual environment handling.
2. **PostgreSQL**: Ensure PostgreSQL is installed and a database is created for this project.

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd FastAPI-TaskManagement-DM
   ```

2. **Install dependencies**:

   ```bash
   poetry install
   ```

3. **Set up the PostgreSQL database**:
   
   Create a PostgreSQL database and configure the connection in `app/config.py`.

4. **Apply migrations**:
   
   Use Alembic (configured in your project) to handle database migrations.

5. **Run the application**:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

6. **Run tests**:

   ```bash
   poetry run pytest
   ```

## API Endpoints

- **`GET /tasks`**: Retrieve all tasks.
- **`POST /tasks`**: Create a new task.
- **`GET /tasks/{task_id}`**: Retrieve a task by ID.
- **`PUT /tasks/{task_id}`**: Update a task by ID.
- **`DELETE /tasks/{task_id}`**: Delete a task by ID.
- **`PATCH /tasks/{task_id}`**: Partially update a task by ID.

## OpenAPI Documentation

After starting the server, access the API documentation at:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Running Tests

All tests are located in the `tests/` directory. Run tests using:

```bash
poetry run pytest
```
