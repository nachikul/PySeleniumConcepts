pipeline {
    agent any
    options {
        // Discard old builds to save storage
        buildDiscarder(logRotator(numToKeepStr: '10'))
        // Set timeout for the pipeline to avoid hangs
        timeout(time: 60, unit: 'MINUTES')
        // Timestamp the output for easier debugging
        timestamps()
    }
    environment {
        // Define global environment variables
        PROJECT_NAME = 'my-awesome-project'
        DEPLOY_ENV = 'staging'
    }
    stages {
        stage('Preparation') {
            steps {
                echo "Preparing pipeline for ${env.PROJECT_NAME} in ${env.DEPLOY_ENV} environment."
                // Pull dependencies, set up necessary tools, etc.
            }
        }
        
        stage('Build') {
            parallel {
                stage('Build Service A') {
                    steps {
                        echo 'Building Service A...'
                        // Custom build steps for Service A
                    }
                }
                stage('Build Service B') {
                    steps {
                        echo 'Building Service B...'
                        // Custom build steps for Service B
                    }
                }
            }
        }
        
        stage('Unit Tests') {
            parallel {
                stage('Unit Test Service A') {
                    steps {
                        echo 'Running unit tests for Service A...'
                        // Run tests, e.g., sh 'npm test' or sh './gradlew test'
                    }
                }
                stage('Unit Test Service B') {
                    steps {
                        echo 'Running unit tests for Service B...'
                        // Run tests, e.g., sh 'npm test' or sh './gradlew test'
                    }
                }
            }
        }

        stage('Static Code Analysis') {
            steps {
                echo 'Running static code analysis...'
                // Run linting, security checks, or code quality analysis (e.g., SonarQube)
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                // Integration tests across services or systems
            }
        }

        stage('Packaging') {
            steps {
                echo 'Packaging the application...'
                // Package artifacts for deployment, e.g., creating Docker images or JARs
            }
        }

        stage('Deployment') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying ${env.PROJECT_NAME} to ${env.DEPLOY_ENV} environment..."
                // Deploy to staging, production, or other environments
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            cleanWs() // Clean up the workspace
        }
        success {
            echo 'Pipeline succeeded!'
            // Notify on success, e.g., sending Slack or email notifications
        }
        failure {
            echo 'Pipeline failed!'
            // Notify on failure, e.g., sending Slack or email notifications
        }
        unstable {
            echo 'Pipeline is unstable!'
            // Handle unstable builds, possibly alerting the team
        }
    }
}
