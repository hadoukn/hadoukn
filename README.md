hadoukn
========

- Setup the master machine using ansible.

  ```bash
  cd ..
  git clone https://github.com/hadoukn/hadouknstack.git
  cd hadouknstack

  virtualenv env
  . env/bin/activate
  pip install ansible
  vagrant up
  ```

- Log into the master and clone hadoukn.

  ```bash
  vagrant ssh
  cd /opt/webapp/hadoukn
  ```

- Install the hadoukn requirements.

  ```bash
  virtualenv env
  env/bin/pip install -r requirements.txt
  ```

- Start the server.

  ```bash
  env/bin/pserve development.ini
  ```
