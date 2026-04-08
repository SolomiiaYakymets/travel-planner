# Travel Planner API

## Requirements

- Python 3.12+
- [Docker](https://www.docker.com/) (optional, for containerized deployment)

---

## Setup

### Using Python

1. **Create and activate a virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the application**:
```bash
uvicorn main:app --reload
```

### Using Docker

1. **Build the image**:
```bash
docker build -t travel-planner .
```

2. **Run the container**:
```bash
docker run -d -p 8000:8000 travel-planner
```

---

## API Documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## API Groups (Tags)

- `projects`
- `places`

## Endpoint Overview

### Projects

- `POST /projects/` - Create project
- `GET /projects/` - List projects
- `GET /projects/{project_id}` - Get project by ID
- `PUT /projects/{project_id}` - Update project
- `DELETE /projects/{project_id}` - Delete project

### Places

- `POST /places/projects/{project_id}` - Add place to project
- `PUT /places/{place_id}` - Update place
- `GET /places/{project_id}/places/` - List places in project
- `GET /places/{project_id}/places/{place_id}` - Get place in project

## Main Request and Response Schemas

### ProjectCreate

- `name` (`str`, required)
- `description` (`str | null`)
- `start_date` (`date | null`)
- `places` (`PlaceRead[] | null`)

### ProjectUpdate

- `name` (`str | null`)
- `description` (`str | null`)
- `start_date` (`date | null`)

### ProjectRead

- `id` (`int`)
- `name` (`str`)
- `description` (`str | null`)
- `start_date` (`date | null`)
- `completed` (`bool`)
- `places` (`PlaceRead[]`)

### PlaceCreate

- `external_id` (`int`, required)
- `notes` (`str | null`)

### PlaceUpdate

- `notes` (`str | null`)
- `visited` (`bool | null`)

### PlaceRead

- `id` (`int`)
- `external_id` (`int`)
- `name` (`str`)
- `notes` (`str | null`)
- `visited` (`bool`)
