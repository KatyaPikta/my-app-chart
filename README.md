## Запуск кластера k8s

Для запуска приложения можно использовать minikube
Сначала его нужно установить 
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```
После установки запустить кластер
```bash
minikube start
```

## Установка self-hosted CI/CD runner

Для настройки runner создайте директорию и скачайте пакет для установки
```bash
 mkdir actions-runner && cd actions-runner
 curl -o actions-runner-linux-x64-2.328.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.328.0/actions-runner-linux-x64-2.328.0.tar.gz
 tar xzf ./actions-runner-linux-x64-2.328.0.tar.gz
```
## Конфигурация runner

Запустите конфигурацию (команды из GitHub интерфейса).
Указываем свой репозиторий и токен раннера, который добавили к своему репозиторию в github.com

```bash
cd actions-runner
./config.sh --url https://github.com/your-username/your-repo --token YOUR_TOKEN
```
## Установить как службу

```bash
cd actions-runner
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status #просмотр статус службы раннера
```

## Подключение docker.io registry

- После создания докер-образов для backend и frontend нужно их отправить в репозиторий, для этого подключаем docker.io registry
- Создаем два репозитория my-frontend и my-backend на dockerhub
- создаем acces token на docker hub и коируем его на github, и создаем два секрета: DOCKERHUB_USERNAME и DOCKERHUB_TOKEN

## Как работает пайплайн

- Для pull/merge реквестов проверяется сборка, выполняются тесты.
- Для слияния в основную ветку: выполняются все этапы пайплайна

## Установка и создание структуры Helm chart

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm create my-app-chart
```

## Комментарии

- для установки и запуска minkube нужно убедиться что у пользователя достаточно прав, чтобы работать с docker

```bash
sudo usermod -aG docker $USER

```