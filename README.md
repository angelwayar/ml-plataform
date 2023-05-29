# Description

Machine Learning Platform (MLP)

## Tasks

| Task | In Progress | Blocked | QA  | Done |
|------|-------------|---------|-----|------|
| 1    |             |         | -   | [x]  |
| 2    |             |         | -   | [x]  |
| 3    |             |         | -   | [x]  |
| 4    |             |         | -   | [x]  |
| 5    |             |         | -   | [x]  |
| 6    |             |         | -   | [x]  |
| 7    |             |         | [x] | [ ]  |
| 8    |             |         | -   | [x]  |
| 9    |             |         | -   | [x]  |
| 10   |             |         | -   | [x]  |
| 11   |             |         | [x] | [ ]  |
| 12   |             |         |     | [x]  |
| 13   |             |         |     | [x]  |
| 14   |             |         |     | [x]  |
| 15   |             |         |     | [x]  |
| 16   |             |         | [x] | [ ]  |
| 17   |             |         | [x] | [ ]  |
| 18   |             |         | [x] | [ ]  |
| 19   |             |         | [x] | [ ]  |


### Tasks

1. Create user model_views User(username, password)
2. Create user entity UserEntity(username, password)
3. Create user models User(id, username, password, created_at, updated_at, is_deleted)
4. Create user repository and its implementation
5. Create unit work of user
6. Create dependencies
7. Create endpoint create_user
8. Encrypt the password
9. Validate email
10. Error manager
11. Create endpoint login  
12. Create image entity
13. Create model Image(id, ide_user, image_base64)
14. Implement ml_model
15. Repository
16. Endpoint get all image
17. Endpoint get image by id
18. Endpoint Update image
19. Endpoint Delete image

## Architecture

```text
app
├── core
|   └──feature
|       ├──models
|       ├──errors
|       ├──use_cases
|       ├──unit_of_work
|       ├──ai_models
|       ├──database
|       ├──errors
|       ├──services
|       ├──token
|       ├──utils
|       └──repositories
├── api
|   └──feature
|       └──routes
├── domain
|   └──feature
|       ├──use_cases
|       ├──entities
|       ├──services
|       └──repositories
├──  data
|    └──feature
|       ├──models
|       ├──repositories_impl
|       └──services 
```
