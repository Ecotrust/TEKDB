# TEKDB ![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/paigewilliams/9ac2331c0af09d1f4fc3921a2c2cd142/raw/coverage-badge.json)

Traditional Ecological Knowledge Ethnographic Database Application

## [Development Installation](https://github.com/Ecotrust/TEKDB/wiki/Development-Installation) 

## [Running Tests](https://github.com/Ecotrust/TEKDB/wiki/Running-tests)

## Development Cycle

This project aims to follow a specific development cycle to ease collaboration and keep the different environments in sync. Below is a diagram of what the development lifecycle should look like:

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
        DEVMERGE --> GHSTAGE[GitHub Action deploys to staging.itkdb.org]
        GHSTAGE --> QA[QA on staging environment]
        QA --> QAPASS{Passes QA}
    end

    subgraph Production
        QAPASS -->|PASSES| PRVERSION[Create feature branch and open PR to update version in settings.py]
        QAPASS -->|FAILS| FEAT
        PRVERSION --> PRDEV[Merge into develop branch]
        PRDEV --> PRMAIN[PR for develop into main]
        PRMAIN --> PRMERGEMAIN[Merge into main branch]
        PRMERGEMAIN --> RELEASE[Publish a new Release]
        RELEASE --> GHPROD[GitHub Action builds and publishes images to GHCR]
        GHPROD --> PRODDEPLOY[Manually deploy to demo.itkdb.org]
        PRODDEPLOY --> QAPROD[Test in production]
        QAPROD --> QAPASSPROD{Passes QA}
        QAPASSPROD --> |PASSES| SUCCESS[Success!]
        QAPASSPROD --> |Fails| HOTFIX[Create a hotfix branch off of main]
        HOTFIX --> PRHOTFIX[PR for hotfix into main]
        PRHOTFIX --> APPROVEHOTFIX{Approval}
        APPROVEHOTFIX --> |Approval| MERGEHOTFIX[Merge into main branch]
        APPROVEHOTFIX --> |Rejected| REJECTEDHOTFIX[Address feedback]
        REJECTEDHOTFIX --> APPROVEHOTFIX
        MERGEHOTFIX --> RELEASE
    end
```
