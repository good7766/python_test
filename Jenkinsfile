pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Ansible Deploy') {
            steps {
                sshagent(credentials: ['ansible-target-ssh']) {
                    sh '''
                        ansible-playbook -i hosts deploy.yml
                    '''
                }
            }
        }
    }
}
