## Architecture

Code architecture follows hexagonal architecture principles, also known as *ports and adapters*.

This architecture is divided in three main layers:

- **Infrastructure**:  The outer layer. Controllers and all I/O related stuff (web framework, DB, ...). Anything that can change by an "external" cause (not by your decision), is in this layer. It includes repositories specific implementation, known as *adapters*.

- **Application**: Use cases. Actions triggered by API calls, represented by application services.

- **Domain**: Inner layer. Business context and rules goes here, represented by models and domain services. Repositories Interfaces, known as *ports*, belongs to this layer.


![hexagona_architecture_schemma](https://github.com/serfer2/flask-hexagonal-architecture-api/blob/main/img/hexagona_architecture_schemma.png)
