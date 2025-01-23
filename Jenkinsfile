pipeline {
    agent any

    environment {
        // Set the timestamp in the environment block
        TIMESTAMP = "${new Date().format('yyMMdd_HHmmss')}"
        BASE_RESULTS_FOLDER = 'results-folder'
        ALLURE_RESULTS = "${BASE_RESULTS_FOLDER}/allure-results_${TIMESTAMP}"
    }

    stages {
        stage('Preparation') {
            steps {
                // Echo the timestamp and allure results folder for debugging
                echo "Timestamp: ${env.TIMESTAMP}"
                echo "Allure Results Folder: ${env.ALLURE_RESULTS}"
            }
        }

        stage('Checkout') {
            steps {
                // Checkout the project repository
                git 'https://github.com/or-kol/sauceDemoProject.git'
            }
        }

        stage('Create Allure Results Folder') {
            steps {
                script {
                    // Create allure results folder if it doesn't exist
                    sh """
                        if [ ! -d "${env.ALLURE_RESULTS}" ]; then
                            mkdir -p "${env.ALLURE_RESULTS}"
                        fi
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest with allure results output directory
                    sh """
                        pytest --alluredir="${env.ALLURE_RESULTS}" -v
                    """
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Generate Allure report
                    sh """
                        allure generate "${env.ALLURE_RESULTS}" -o "${env.WORKSPACE}/allure-report" --clean
                    """
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    results: [
                        "${env.WORKSPACE}/allure-results_${env.TIMESTAMP}"
                    ]
                ])
            }
        }
    }
    
    post {
        always {
            // Cleanup (if needed)
            echo "Build completed with timestamp: ${env.TIMESTAMP}"
        }
    }
}
