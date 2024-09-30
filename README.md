# Twitter-Data-ETL-Pipeline-With-Airflow
This repository includes airflow dags and python pipeline script to Extract Transform and Load data from twitter using API.


**Step 1: Fetch a data from Twitter API. [Do not work as because twitter free API do not provide data now]**

	Step 1.1: Create a project and app in twitter developer portal. Save a app details for later use.(Tweets data is not available in free trial account).
		Twitter API details
  
		Default project-1836677363272491008
		App id- 293568912363
		API key - VapojCQtfGTHISISDUMMYgwKioZDkWTrkjez
		API key secret - TyftltWTHISISDUMMYNUyDCggh889882wBSveI2VW15JabAYJnvFEAxWdyCA1MQlsLabn
		Bearer token - AAAAAAAAAAAAAAAAAAAAAE67TdvwEAAAAAK0GWJ7THISISDUMMYlz0HxadlVCDgBPRDSS87870TY%3D4Ln2mD4WqBEhW8XHz9xNk5gC5yvty5qVCNmvfeMwsrsPQnkRh3
		Access Token- 767385476831469568-i35qK77uyhjhjhuZSITHISISDUMMYDV1AmUCfxzSxgzBZnGoUeQ
		Access Token Secret - WXYuS5Xtxxlmmi04mughtTHISISDUMMY7kkl46246yh6y69Gq6niyLpbfs8621ycVUH8ex
  
		
	Step 1.2: Create Python project. Create a python (script) ETL using tweepy library.

	
**Step 2: Create cloud bucket to store transformed data.**
	create a s3 bucket and assign a IAM role allowing All permissions to the bucket.

**Step 3: Create EC2 instance.[Could not install airflow on free EC2 instance as because free tier do not provide 2GB RAM which is necessary for the Airflow.]**
		pem file is F:\DATA ENGINEERING\portfolio projects\twitterAnalysis>
		3.1 ssh -i "data_engineering_portfolio.pem" ubuntu@ec2-13-201-2-1.ap-south-1.compute.amazonaws.com
		
		3.3 Setup python environment on the server to run the ETL script.
			Install necessary python libraries on the server.
			
			sudo apt-get update
			sudo apt install python3
			sudo apt install python3-pip
			
			sudo apt install python3-venv
			python -m venv tutorial-env
			source twitter-venv/bin/activate
			
			sudo pip install apache-airflow
			sudo pip install pandas
			sudo pip install s3fs
			
		3.4 Run the airflow on virtual environment
			airflow standalone
			
**Step 4: Hence installed airflow on WLS2.**
	Referrence		 Ubuntu on windows
	
	Ubuntu on windows
	References: https://www.freecodecamp.org/news/install-apache-airflow-on-windows-without-docker/#:~:text=To%20work%20with%20Airflow%20on,to%20install%20the%20virtualenv%20package.


	To restart any service on WSL Ubuntu
	sudo /etc/init.d/airflow restart

	To start airflow server.
	==========================
	Switch on ubuntu machine.

	activate virtual environment
	source airflow_venv/bin/activate
	cd airflow
	airflow webserver &
	airflow scheduler

**Step 5: Once airflow is up and unning. Create twitter_dags folder and push all python dags and ETL script to the folder. and configure the directory path in airflow.cfg**
