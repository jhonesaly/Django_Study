# Gunicorn

![logo](gunicorn.png)

Gunicorn é um servidor web Python HTTP que funciona como um gateway entre uma aplicação web Python e a internet. O nome Gunicorn vem de "Green Unicorn", que faz referência ao fato de que o servidor é capaz de lidar com múltiplas conexões simultâneas (de forma "verde" ou "eficiente").

Gunicorn é usado para servir aplicativos Python que usam a especificação WSGI (Web Server Gateway Interface). WSGI é uma interface padrão de comunicação entre um servidor web e uma aplicação web Python. A especificação WSGI permite que diferentes servidores web, como o Gunicorn, Apache ou Nginx, comuniquem-se com aplicativos web Python de maneira consistente.

Ao usar o Gunicorn para hospedar um aplicativo Python, você pode se beneficiar de sua capacidade de lidar com várias solicitações de usuários simultâneas, tornando a aplicação escalável e eficiente. Além disso, o Gunicorn possui recursos de processamento de solicitações em paralelo, o que permite que o servidor processe várias solicitações simultaneamente sem bloquear o processamento de outras solicitações.

Resumindo, o Gunicorn é um servidor web Python HTTP usado para hospedar aplicativos web Python que usam a especificação WSGI. É uma ferramenta importante para tornar aplicativos web escaláveis, eficientes e capazes de lidar com várias solicitações simultâneas.

