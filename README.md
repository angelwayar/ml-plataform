# Description

Machine Learning Platform (MLP)

## Tasks

|       Task     | In Progress | Blocked | QA  | Done |
|----------------|-------------|---------|-----|------|
|        1       |             |         | -   | [x]  |
|        2       |             |         | -   | [x]  |
|        3       |             |         | -   | [x]  |
|        4       |             |         | -   | [x]  |
|        5       |             |         | -   | [x]  |
|        6       |             |         | -   | [x]  |
|        7       |             |         | [x] | [ ]  |
|        8       | [ ]         | [ ]     | [ ] | [ ]  |
|        9       | [ ]         | [ ]     | [ ] | [ ]  |

### Tasks from 14-05-2023/15-05-2023

1. Create user model_views User(username, password)
2. Create user entity UserEntity(username, password)
3. Create user models User(id, username, password, created_at, updated_at, is_deleted)
4. Create user repository and its implementation
5. Create unit work of user
6. Create dependencies
7. Create endpoint create_user
8. Create endpoint login
9. Create endpoint logout

## Architecture

```text
app
├── core
|   ├──models
|   ├──errors
|   ├──use_cases
|   ├──work_units-(base_unit_of_work)
|   └──repositories
|
├── api
|   └──routes
|
├── application
|   ├──model_views -> Puede que esto no pertenezca a esta capa
|   ├──commands -> Implementacion del caso de uso
|   └──queries -> Implementacion del caso de uso
|
├── domain
|   ├──use_cases -> Receive a create_model_view
|   ├──entities
|   ├──repositories
|   └──unit_of_work
|
└── infrastructure
    ├──repositories_impl
    └──schemas-(DTO) 
```
