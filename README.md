# cloud-wiz-fmops
FMOops platform that can be used in real life through generative AI

# Install & Start
```
sudo npm install && sudo npm start
```
# Fast API Docs

http://localhost:8000/docs#/

# Database Session
### SQLALCHEMY
```
python
db: Session = Depends(lambda: get_database(ServiceType.SQLALCHEMY))
```
### MYSQL
```
python
db: Session = Depends(lambda: get_database(ServiceType.MYSQL))
```
### SQLITE
```
python
db: Session = Depends(lambda: get_database(ServiceType.SQLITE))
```

# GIT
### connection
```
git remote add origin https://github.com/easyooops/cloud-wiz-fmops.git

git remote -v
```
### create branch
```
# git checkout -b [new branch]
git checkout -b feature-suyeong

git branch
```
### Pull Request
```
git add .

# git commit -m "[comment]"
git commit -m "add frontend"

# git push origin [new branch]
git push origin feature-suyeong
```
### Pull Main
```
git pull origin main
```

# alembic

### 마이그레이션 생성
```
alembic revision --autogenerate -m "edit agent table"
```

### 마이그레이션 적용
```
alembic upgrade head
```