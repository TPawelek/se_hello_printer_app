Skip to content
Search or jump to…
Pulls
Issues
Marketplace
Explore

@TPawelek
YuiKinoko
/
se_hello_printer_app
Public
forked from wojciech11/se_hello_printer_app
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
se_hello_printer_app/Jenkinsfile
@YuiKinoko
YuiKinoko wyglad Jenkinsfile
Latest commit ca0ece1 32 minutes ago
 History
 2 contributors
@YuiKinoko@skarab7
49 lines (48 sloc)  1.39 KB

pipeline {
    agent any
    stages {

        stage('Deps') {
            steps {
	            sh 'make deps'
            }
        }
        stage('Test') {
            steps {
                sh 'make test_xunit || true'
                xunit thresholds: [
	                skipped(failureThreshold: '0'),
	                failed(failureThreshold: '1')
	            ],
	            tools: [
	                JUnit(deleteOutputFiles: true,
	                failIfNotNew: true,
	                pattern: 'test_results.xml',
	                skipNoTestFiles: false,
	                stopProcessingIfError: true)
	            ]
            }
        }
        stage('Linter') {
            steps {
                sh 'make lint'
            }
        }
    }
    post{
        always{
            chuckNorris()
            cobertura autoUpdateHealth: false,
                      autoUpdateStability: false,
                      coberturaReportFile: 'coverage.xml',
                      conditionalCoverageTargets: '70, 0, 0',
                      failUnhealthy: false,
                      failUnstable: false,
                      lineCoverageTargets: '80, 0, 0',
                      maxNumberOfBuilds: 0,
                      methodCoverageTargets: '80, 0, 0',
                      onlyStable: false,
                      sourceEncoding: 'ASCII',
                      zoomCoverageChart: false
        }
    }
}
