# TEKDB ![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/paigewilliams/9ac2331c0af09d1f4fc3921a2c2cd142/raw/coverage-badge.json)

Traditional Ecological Knowledge Ethnographic Database Application

## [Development Installation](https://github.com/Ecotrust/TEKDB/wiki/Development-Installation) 

## [Running Tests](https://github.com/Ecotrust/TEKDB/wiki/Running-tests)

## CI/CD 

This project has a few Github actions that run to have continous integration / continuous deployment with our environments. Below is a diagram on the path to production:

```mermaid
flowchart TB
    subgraph Develop
        CHECKOUT[checkout develop branch] --> FEAT[Create feature Branch]
        FEAT --> PR[Submit Pull Request against develop branch]
        PR --> APPROVE{Approval}
        APPROVE -->|Approved| DEVMERGE[Merge into develop branch]
        APPROVE -->|Rejected| REJECTED[Address feedback]
        REJECTED --> APPROVE
    end

    subgraph Staging
        DEVMERGE --> GHSTAGE[Github Action deploys to staging.itkdb.org]
        GHSTAGE --> QA[QA on staging environment]
        QA --> QAPASS{Passes QA}
        QAPASS -->|PASSES| PRVERSION[Create PR to update version in settings.py]
        QAPASS -->|FAILS| FEAT
        PRVERSION --> PRDEV[Merge into develop branch]
    end

    subgraph Production
        PRDEV --> PRMAIN[PR for develop into main]
        PRMAIN --> RELEASE[Publish a new Release]
        RELEASE --> GHPROD[Github Action builds and publishes images to GHCR]
        GHPROD --> PRODDEPLOY[Manually deploy to demo.itkdb.org]
    end
```
