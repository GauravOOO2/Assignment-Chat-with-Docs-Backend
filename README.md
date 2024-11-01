# Document Management System with NLP and RAG Integration

## Overview

This project is a secure, scalable, full-stack application that allows users to upload, store, and interact with various document types (e.g., PDF, PPT, CSV) using advanced Natural Language Processing (NLP). A RAG (Retrieve and Generate) Agent is implemented to query documents with user questions. This solution supports document management, user authentication, and effective NLP-based querying, utilizing `unstructured.io` for efficient document parsing.

## Technologies

- **Backend**: FastAPI
- **Frontend**: React.js
- **Database**: PostgreSQL, Redis
- **File Storage**: AWS S3 (or equivalent)
- **Document Parsing**: `unstructured.io` for text and metadata extraction
- **NLP Processing**: LangChain/LLamaIndex
- **Agents**: Autogen/Crewai (or equivalent)
- **Search Engine**: Elasticsearch
- **Authentication**: Session-based (OAuth2.0 or JWT as alternatives)
- **Deployment**: Docker, Kubernetes

## Features

### Document Upload and Management
- **Multi-format Support**: Upload and store documents in various formats (PDF, PPT, CSV, etc.) securely.
- **Real-time Parsing**: Automatic text and metadata extraction using `unstructured.io`.
- **Storage**: AWS S3 (or equivalent) ensures document durability and accessibility.

### Advanced NLP Features with RAG Agents
- **Contextual Query Handling**: Retrieve and generate answers based on stored document content.
- **NLP Processing**: LangChain/LLamaIndex for document indexing and search.
- **Response Generation**: Autogen/Crewai agents provide context-aware answers.

### Additional Functionalities
- **Authentication**: Secure user login with session management.
- **Usability**: User-friendly interface for ease of use.
- **Scalability**: Supports complex NLP queries with efficient resource use.

## Architecture

This application consists of a microservices architecture where:
1. **Frontend Service**: React.js UI for document upload, query input, and response display.
2. **Backend Service**: FastAPI server handling document management, NLP processing, and RAG agent querying.
3. **Database**: PostgreSQL for structured data and Redis for cache management.
4. **File Storage**: AWS S3 for document storage.
5. **Search and Indexing**: Elasticsearch for quick document retrieval.
6. **Document Parsing Service**: `unstructured.io` for document text and metadata extraction.

## Database Schema

- **Documents**: Stores document metadata, format, and related attributes.
- **Users**: Manages user authentication and session data.
- **Queries**: Logs user queries and response history.

## Setup and Installation

### Prerequisites
- Docker, Docker Compose
- Kubernetes (optional for deployment)
- PostgreSQL, Redis, and AWS S3 credentials

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Environment Variables**: Configure environment variables for database, AWS S3, and other integrations.

3. **Database Setup**
   - Run PostgreSQL and Redis containers:
     ```bash
     docker-compose up -d postgres redis
     ```
   - Apply migrations to initialize the database schema.

4. **Backend Service**:
   - Install dependencies and start the FastAPI server:
     ```bash
     cd backend
     pip install -r requirements.txt
     uvicorn main:app --reload
     ```

5. **Frontend Service**:
   - Navigate to the `frontend` folder, install dependencies, and start the React app:
     ```bash
     cd frontend
     npm install
     npm start
     ```

6. **Elasticsearch Setup**:
   - Ensure Elasticsearch is running and configured with appropriate indices.

### Docker Deployment

1. **Build Docker Images**:
   ```bash
   docker-compose build
   ```

2. **Run Docker Containers**:
   ```bash
   docker-compose up
   ```

### Kubernetes Deployment (Optional)

- Deploy the app components with Kubernetes manifests:
  ```bash
  kubectl apply -f k8s/
  ```

### Monitoring and Logging (Optional)

- **Monitoring**: Use Prometheus and Grafana for collecting metrics and dashboard visualization.
- **Logging**: Configure ELK Stack for log aggregation and visualization.

## Usage

1. **User Authentication**: Register and log in to access the document management features.
2. **Upload Documents**: Upload PDFs, PPTs, or CSV files, which will be parsed and stored.
3. **Ask Questions**: Enter questions related to the uploaded documents. The RAG agent retrieves and generates answers based on document content.

## Evaluation

- **Code Quality**: Clean, modular, and well-documented code.
- **Scalability**: Architected for high availability and fault tolerance.
- **Deployment**: Containerized with optional Kubernetes deployment.
- **Innovation**: Enhanced document interaction through NLP and RAG-based querying.

