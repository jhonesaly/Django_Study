# Criando Cluster

Para criar um cluster Docker Swarm, você precisa ter pelo menos duas máquinas com o Docker Engine instalado. Você pode criar um cluster usando o comando "docker swarm init" no terminal de uma das máquinas. Isso iniciará o cluster e transformará a máquina em um nó de gerenciamento. Ele também gerará um token de união que você pode usar para adicionar outros nós ao cluster.

Aqui estão os passos para criar um cluster Docker Swarm:

- Certifique-se de que as máquinas que você deseja adicionar ao cluster tenham o Docker Engine instalado.
- Execute o comando "docker swarm init" em uma das máquinas para iniciar o cluster e transformá-la em um nó de gerenciamento.
- Anote o token de união gerado pelo comando "docker swarm init".
- Execute o comando "docker swarm join" nas outras máquinas e forneça o token de união para adicioná-las ao cluster.

Não é necessário interromper a operação dos contêineres para criar um cluster Docker Swarm. No entanto, você precisará interromper e remover os contêineres que estão sendo executados em um nó antes de removê-lo do cluster. Isso ocorre porque o Docker Swarm distribui os contêineres entre os nós e, se você remover um nó sem interromper os contêineres, pode perder os dados que estão sendo processados por esses contêineres.

Para criar um cluster de Docker Swarm usando Vms, você precisará seguir os seguintes passos:

- Clone a VM existente que contém o contêiner do MySQL.
- Inicie a VM clonada e certifique-se de que ela esteja conectada à mesma rede que a VM original.
- Certifique-se de que a instalação do Docker Engine esteja funcionando corretamente na VM clonada.
- Inicie o contêiner do MySQL na VM clonada usando o mesmo comando usado na VM original.
- Execute o comando "docker swarm init" na VM original para iniciar o cluster Docker Swarm.
- copie o comando "docker swarm join --token ... 192.168.0.9:2377"

## Comandos

    docker swarm init
    docker swarm join --token ... 192.
    docker stack deploy -c docker-compose.yml <nome_da_stack>
    docker stack rm <nome_da_stack>
    docker swarm leave --force