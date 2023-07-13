name: Feature request
about: Share an idea or make a request to help us improve
description: Create a new ticket for new documentation or material.
title: "🐛 [BUG] - <title>"
assignees: ''
labels: [
  "bug",
  "Docs",
  "Needs Triage"
]
body:
  - type: textarea
    id: problem
    attributes:
      label: Documentation request
      description: >
        Please provide a description of what documentation you believe needs to be fixed,
        improved, or added.
    validations:
      required: true
  - type: textarea
    id: suggested-fix
    attributes:
      label: Suggested fix for documentation
      description: >
        A clear and concise description of what you want to happen.
        Feel free to include any third-party resources if related.
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Problem Description (if any)
      description: >
        A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
    validations:
      required: false
  - type: textarea
    id: alternatives
    attributes:
      label: Describe alternatives you've considered
      description: >
        A clear and concise description of any alternative solutions or features you've considered.
    validations:
      required: false
  - type: textarea
    id: additional-context
    attributes:
      label: Additional context
      description: >
        Add any other context or screenshots about the feature request here.
    validations:
      required: false