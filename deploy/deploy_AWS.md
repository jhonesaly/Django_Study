# Deploy na AWS

## Criando instância EC2

Passo 1: Acesse o Console de Gerenciamento da AWS em https://console.aws.amazon.com/ e faça login na sua conta da AWS.

Passo 2: No painel de navegação do Console da AWS, selecione o serviço EC2. Você será direcionado para o console do EC2.

Passo 3: Clique no botão "Launch Instance" (Iniciar Instância) para começar a configurar sua instância EC2.

Passo 4: Escolha a AMI (Amazon Machine Image) que deseja usar para sua instância EC2. A AMI é essencialmente uma imagem do sistema operacional que você deseja executar na sua instância EC2. Você pode escolher uma AMI fornecida pela AWS ou usar uma AMI personalizada.

Passo 5: Escolha o tipo de instância que deseja usar para sua instância EC2. O tipo de instância é determinado pela quantidade de recursos de CPU, memória, armazenamento e rede que você precisa para sua carga de trabalho.

Passo 6: Configure as opções de rede para sua instância EC2, incluindo a VPC (Virtual Private Cloud), as sub-redes e as regras de segurança de entrada e saída.

Passo 7: Escolha o tamanho e o tipo de armazenamento para sua instância EC2. Você pode escolher entre armazenamento de instância, armazenamento em bloco (EBS) e armazenamento S3.

Passo 8: Configure as opções de inicialização para sua instância EC2, incluindo ações de inicialização, como scripts e comandos de shell que serão executados quando a instância for iniciada.

Passo 9: Revise todas as configurações para garantir que estejam corretas e, em seguida, clique em "Launch" (Iniciar) para iniciar sua instância EC2.

Passo 10: Depois que sua instância EC2 for iniciada, você poderá se conectar a ela usando um cliente SSH. Para isso, selecione sua instância EC2 no console do EC2, clique no botão "Connect" (Conectar) e siga as instruções para se conectar à sua instância.

## Instalando MySQL no servidor

Comandos no server:

    sudo apt update
    sudo apt-get install mysql-server
    sudo apt-get install libmysqlclient-dev
    sudo mysql -u root -p 

    use mysql 
    update user set plugin='mysql_native_password' where user='root';
    flush privileges; 
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root_password';
    exit

    sudo mysql_secure_installation

    sudo mysql -u root -p
    CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'admin_password';
    CREATE DATABASE db_name;
    GRANT ALL PRIVILEGES ON db_name.* TO 'db_admin'@'localhost';
    exit

## Configurando git

Comandos no server:

    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main

## Repositório bare

Comandos no server:

    mkdir -p ~/app_bare
    cd ~/app_bare
    git init --bare
    cd ~

## Repositório da aplicação

Comandos no server:

    mkdir -p ~/app_repo
    cd ~/app_repo
    git init
    git remote add origin ~/app_bare
    git add . && git commit -m 'Initial'
    cd ~

## Fazendo conexão SSH

Comandos no local:

    ssh-keygen
    cat ~/.ssh/id_rsa.pub

Copie a chave ssh mostrada

Comandos no server:

    nano ~/.ssh/authorized_keys

Adicione a chave copiada no local computer na última linha do arquivo, salve e feche

## Copie o app para o server

Comandos no local:

    git remote add app_bare ubuntu@<aws_server_ip>:~/app_bare
    git push app_bare <branch> (master ou main)

Comandos no server:

    cd app_repo
    git pull origin <branch> (master ou main)

## Criando ambiente virtual e instalando pacotes

Comandos no server (na pasta app_repo):
    python -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Caso não tenha feito o arquivo requirements ainda, vá na pasta do projeto e use o seguinte comando:

    pip freeze > requirements.txt

Então refaça o procedimento de push para o mesmo estar disponível no servidor.

Outros pacotes necessários no server:

    pip install psycopg2
    pip install gunicorn
    pip install mysqlclient

Se a installação do psycopg2 não der certo, instale esse pacote antes e repita:

    sudo apt-get install python3-dev

## Configurando o environment

    cp .env-example .env
    nano .env

Coloque as configurações corretas no arquivo
