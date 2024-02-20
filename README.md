# YelpReviews-DataPipeline-aws


# Yelp Restaurants and Bars Dataset

## Overview
This project aims to gather information about restaurants and bars from Yelp, focusing on their names, types, review counts, and other relevant details. The data is then cleaned and stored in a structured format using Apache Airflow, with the dataset residing in an Amazon S3 bucket. An EC2 t2 medium instance hosts Apache Airflow, orchestrating the entire pipeline.

## Dataset Details
The dataset includes the following key attributes:

Name: Name of the restaurant or bar.
Type: Type of establishment (restaurant or bar).
Review-Count: Number of reviews received on Yelp.
Categories: Categories under which the establishment is listed.
Ratings: Ratings given on Yelp.
Latitude, Longitude: Geographical coordinates of the establishment.
Transactions: Types of transactions available.
Address, City, Zipcode, State: Location details.
Phone: Contact number of the establishment.
Distance: Distance from the specified location.


## Apache Airflow Orchestration
The data pipeline is orchestrated using Apache Airflow, hosted on an EC2 t2 medium instance. The workflow involves the following steps:

Data Collection: Yelp API is queried for information on restaurants and bars in various locations.
Data Cleaning: The obtained data is cleaned and structured using the provided ETL function.
Data Storage: The cleaned dataset is then stored in an Amazon S3 bucket.

## ETL Function
The ETL (Extract, Transform, Load) process is handled by the etl_airflow_run() function. This function utilizes the Yelp API to fetch data for restaurants and bars in specified locations. The data is then processed and stored in a CSV file named yelp_reviews.csv.

## S3 Bucket
The structured dataset is stored in an S3 bucket, enabling easy accessibility and scalability.

![s3_bucket_yelp](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/80b9272a-ce8b-483a-8116-e88c693e3eca)


yelp_dataset/
yelp_reviews.csv: Cleaned dataset containing information about restaurants and bars.

## Usage

To run the Apache Airflow pipeline:

1. Ensure that Apache Airflow is correctly installed on the EC2 instance.
2. Configure the necessary connections and variables in the Airflow environment.
3. Copy and paste the provided ETL function into an Airflow DAG (Directed Acyclic Graph) script.
4. Trigger the DAG to initiate the data pipeline.

## EC2 Security Group Settings:
1. Replace your-security-group-id with the actual security group ID and your-ip-range with your IP address or a specific IP range.
2. Allow Inbound Traffic for Apache Airflow Web Server.

   ![ec2_securityaccess](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/c188135e-ca3e-46a2-896d-adb0d1f6cd44)
   Note: The above configuration was created solely for project purpose and is not recommended for industry standards!

## IAM Permissions for EC2 to Access S3:

For this project, I have given the following accesses to EC2 to get a hold of the S3 bucket.
![ec2-s3_permissionaccess](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/7685a3ad-ff07-499c-ad1f-9bf21b9db117)   


## Steps to connect Airflow with EC2 Instance:
1. Use SSH to connect to your EC2 instance. Replace your-ec2-ip and your-key.pem with your EC2 instance's public IP address and the path to your SSH private key file, respectively.

   ![ec2_instance](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/3df2373e-fb97-4273-be23-8ad1e35b8f5f)

   ![ec2-instance-ssh-connectiondetails](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/f2f4987a-1575-4bb3-9236-6b6846b76f58)

3. Update your package manager and install necessary software such as Python, pip, and any other dependencies required for your specific use case.
4. Use pip to install Apache Airflow. It's recommended to install it in a virtual environment.
5. Configure Airflow by creating the necessary directories and modifying the airflow.cfg configuration file.

   ![Screenshot 2024-02-18 130236](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/b393aebb-23fc-4420-bd92-7ce20e1eb3eb)

7. Start the Airflow standalone.

   ![Screenshot 2024-02-18 130131](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/3de5d2b6-316e-4a4f-b876-8d13371bf070)

9. Create your Airflow DAGs (Directed Acyclic Graphs) and place them in the ~/airflow/dags/ or a customized directory. You can use a tool like scp or any SFTP client to transfer files to your EC2 instance.

    ![Screenshot 2024-02-18 152010](https://github.com/Arvind1997/YelpReviews-DataPipeline-aws/assets/13155343/61398c48-0837-45a7-a1c0-942ccf63b83a)

11. Once your DAGs are in place, you can trigger them using the Airflow web interface or the command line.




## Acknowledgments
This project is based on the Yelp API and is intended for educational and analytical purposes. Please review Yelp's terms of service for any usage restrictions or requirements.



