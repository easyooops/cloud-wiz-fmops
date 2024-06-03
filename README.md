# cloud-wiz-fmops
cloud-wiz-fmops

# Install & Start
sudo npm install && sudo npm start

# Fast API Docs
http://localhost:8000/docs#/

# Database Session
### SQLALCHEMY
db: Session = Depends(lambda: get_database(ServiceType.SQLALCHEMY))

### MYSQL
db: Session = Depends(lambda: get_database(ServiceType.MYSQL))

### SQLITE
db: Session = Depends(lambda: get_database(ServiceType.SQLITE))

# GIT
##### connection
git remote add origin https://github.com/easyooops/cloud-wiz-fmops.git
git remote -v

##### create breanch
git checkout -b feature-suyeong
git branch

##### push
git add .
git commit -m "add frontend"
git push origin feature-suyeong