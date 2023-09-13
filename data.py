import pandas as pd

preguntas =[
    {'pregunta': 'A company is planning to run a global marketing application in the AWS Cloud. The application will feature videos that can be viewed by users. The company must ensure that all users can view these videos with low latency. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. AWS Auto Scaling
B. Amazon Kinesis Video Streams
C. Elastic Load Balancing
D. Amazon CloudFront''',
     'respuesta': 'D. Amazon CloudFront',
     'argumento': 'Amazon CloudFront: The best option for the company to ensure that users can view videos with low latency would be to use Amazon CloudFront. CloudFront is a content delivery network (CDN) that speeds up the delivery of static and dynamic web content, such as HTML, CSS, JavaScript, and images, as well as videos.',
     'referencia': 'https://aws.amazon.com/cloudfront/'},
    {'pregunta': 'Which pillar of the AWS Well-Architected Framework refers to the ability of a system to recover from infrastructure or service disruptions and dynamically acquire computing resources to meet demand?',
     'opciones': '''A. Security.
B. Reliability.
C. Performance efficiency. 
D. Cost optimization.''',
     'respuesta': 'Reliability',
     'argumento': 'The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.',
     'referencia': 'https://aws.amazon.com/architecture/well-architected/'},
    {'pregunta': 'A company is planning to replace its physical on-premises compute servers with AWS serverless compute services. The company wants to be able to take advantage of advanced technologies quickly after the migration. Which pillar of the AWS Well-Architected Framework does this plan represent?',
     'opciones': '''A. Security.
B. Performance Efficiency.
C. Operational excelence.
D. Reliability.''',
     'respuesta': 'Performance efficiency',
     'argumento': 'The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.',
     'referencia': 'https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework/'},
    {'pregunta': 'A large company has multiple departments. Each department has its own AWS account. Each department has purchased Amazon EC2 Reserved Instances. Some departments do not use all the Reserved Instances that they purchased, and other departments need more Reserved Instances than they purchased. The company needs to manage the AWS accounts for all the departments so that the departments can share the Reserved Instances. Which AWS service or tool should the company use to meet these requirements?',
     'opciones': '''A. AWS Systems Manager. 
B. Cost Explorer. 
C. AWS Trusted Advisor. 
D. AWS Organizations.''',
     'respuesta': 'AWS Organizations',
     'argumento': 'By using AWS Organizations, the company can also implement service control policies (SCPs) to enforce resource sharing and usage policies across the organization. This way, departments that have excess Reserved Instances can allocate them to departments that need additional capacity.',
     'referencia': 'https://docs.aws.amazon.com/ram/latest/userguide/what-is.html'},
    {'pregunta': 'Which of the following are benefits of migrating to the AWS Cloud? (Choose two.)',
     'opciones': '''A. Operational resilience. 
B. Discounts for products on Amazon.com. 
C. Business agility. 
D. Business excellence. 
E. Increased staff retention''',
     'respuesta': '''A. Operational resilience. 
B. Business agility''',
     'argumento': 'Operational resilience: The AWS Cloud is designed to be highly available and scalable, which can help organizations improve their operational resilience and reduce the impact of failures or disruptions. Business agility: Migrating to the AWS Cloud can help organizations to increase their business agility by allowing them to quickly and easily deploy new applications and services, scale their infrastructure up or down as needed, and experiment with new technologies.',
     'referencia': 'https://www.easydeploy.io/blog/benefits-of-aws-migration/'}, #5
    {'pregunta': 'Which component of the AWS global infrastructure is made up of one or more discrete data centers that have redundant power, networking, and connectivity?',
     'opciones': '''A. AWS Region. 
B. Availability Zone. 
C. Edge location. 
D. AWS Outposts.''',
     'respuesta': 'Availability Zone',
     'argumento': 'An Availability Zone (AZ) is a physically separate data center within an AWS Region. Each Availability Zone has its own power source, networking infrastructure, and connectivity. They are designed to be isolated from failures in other Availability Zones within the same Region. The purpose of Availability Zones is to provide fault tolerance and high availability for applications and services hosted in the AWS cloud. By deploying resources across multiple Availability Zones, organizations can ensure that their systems remain operational even if an individual Availability Zone experiences an outage.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html'},
    {'pregunta': 'Which duties are the responsibility of a company that is using AWS Lambda? (Choose two.)',
     'opciones': '''A. Security inside of code.
B. Selection of CPU resources.
C. Patching of operating system.
D. Writing and updating of code.
E. Security of underlying infrastructure.''',
     'respuesta': '''A. Security inside of code. 
D. Writing and updating of code''',
     'argumento': 'Security inside of code: It is the company´s responsibility to ensure the security of the code running within the Lambda functions. This includes implementing proper security measures, such as input validation, encryption, and access controls, to protect the code and the data it processes. Writing and updating of code: The company is responsible for developing and maintaining the code that runs within the Lambda functions. This involves writing the code, testing it, and making any necessary updates or modifications over time.',
     'referencia': 'https://aws.amazon.com/lambda/features/'},
    {'pregunta': 'Which AWS services or features provide disaster recovery solutions for Amazon EC2 instances? (Choose two.)',
     'opciones': '''A. Reserved Instances.
B. EC2 Amazon Machine Images (AMIs).
C. Amazon Elastic Block Store (Amazon EBS) snapshots.
D. AWS Shield.
E. Amazon GuardDuty.''',
     'respuesta': '''B. EC2 Amazon Machine Images (AMIs).
C. Amazon Elastic Block Store (Amazon EBS) snapshots''',
     'argumento': 'Amazon Elastic Block Store (Amazon EBS) snapshots: Amazon EBS is a block storage service for use with Amazon EC2 instances. EBS snapshots are point-in-time copies of an EBS volume that can be used to create a new volume or restore an existing volume. EBS snapshots can be used to recover data in the event of an instance failure, or to create a new instance in a different region or Availability Zone. Amazon Machine Images (AMIs): An AMI is a pre-configured virtual machine image that contains the operating system, application software, and any other required components needed to launch an instance. AMIs can be used to create new instances in the same or a different region, which can be useful for disaster recovery purposes.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html'},
    {'pregunta': 'A company is migrating to the AWS Cloud instead of running its infrastructure on premises. Which of the following are advantages of this migration? (Choose two.)',
     'opciones': '''A. Elimination of the need to perform security auditing.
B. Increased global reach and agility, Ability to deploy globally in minutes.
C. Elimination of the cost of IT staff members.
D. Redundancy by default for all compute services.''',
     'respuesta': 'Increased global reach and agility, Ability to deploy globally in minutes',
     'argumento': 'Increased global reach and agility: AWS offers a global network of data centers, enabling businesses to deploy their applications and services in multiple regions around the world. This global reach allows for reduced latency and improved performance for users in different geographical locations. Additionally, AWS provides various services and tools that enhance agility, enabling businesses to quickly scale their resources up or down as needed, and rapidly innovate and deploy new solutions. Ability to deploy globally in minutes: With AWS´s global infrastructure, businesses can quickly deploy their applications and services to multiple regions around the world. This allows them to serve their customers with low latency and high availability in various geographic locations. AWS provides automation and management tools that facilitate fast and efficient deployment across regions.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'A user is comparing purchase options for an application that runs on Amazon EC2 and Amazon RDS. The application cannot sustain any interruption. The application experiences a predictable amount of usage, including some seasonal spikes that last only a few weeks at a time. It is not possible to modify the application. Which purchase option meets these requirements MOST cost-effectively?',
     'opciones': '''A. Review the AWS Marketplace and buy Partial Upfront Reserved Instances to cover the predicted and seasonal load. 
B. Buy Reserved Instances for the predicted amount of usage throughout the year.  
C. Allow any seasonal usage to run at an On-Demand rate.
D. Buy Reserved Instances to cover all potential usage that results from the seasonal usage.''',
     'respuesta': 'Buy Reserved Instances for the predicted amount of usage throughout the year. Allow any seasonal usage to run at an On-Demand rate.',
     'argumento': 'buying Reserved Instances for the predicted amount of usage throughout the year and allowing any seasonal usage to run at an On-Demand rate, provides a balance between cost optimization and ensuring uninterrupted service. By using Reserved Instances for the predictable usage and leveraging On-Demand instances for seasonal spikes, the user can avoid overprovisioning while still having the required capacity during peak periods. This approach allows for cost-effective utilization of resources while meeting the application´s requirement of no interruptions.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html'}, #10
    {'pregunta': 'A company wants to review its monthly costs of using Amazon EC2 and Amazon RDS for the past year. Which AWS service or tool provides this information?',
     'opciones': '''A. AWS Trusted Advisor. 
B. Cost Explorer. 
C. Amazon Forecast. 
D. Amazon CloudWatch.''',
     'respuesta': 'Cost Explorer',
     'argumento': 'Cost Explorer is a powerful AWS tool that allows users to analyze and visualize their AWS costs and usage over time. It provides various features to understand, explore, and manage costs effectively. With Cost Explorer, users can view their monthly costs and usage for specific AWS services, including Amazon EC2 and Amazon RDS. It offers pre-built reports, customizable filters, and visualizations to help analyze spending patterns, identify cost drivers, and track expenses over time.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'},
    {'pregunta': 'A company wants to migrate a critical application to AWS. The application has a short runtime. The application is invoked by changes in data or by shifts in system state. The company needs a compute solution that maximizes operational efficiency and minimizes the cost of running the application. Which AWS solution should the company use to meet these requirements?',
     'opciones': '''A. Amazon EC2 On-Demand Instances. 
B. AWS Lambda. 
C. Amazon EC2 Reserved Instances. 
D. Amazon EC2 Spot Instances''',
     'respuesta': 'AWS Lambda',
     'argumento': '''AWS Lambda
        1. Run code without provisioning or managing infrastructure. Simply write and upload code as a .zip file or container image.
        2. Automatically respond to code execution requests at any scale, from a dozen events per day to hundreds of thousands per second.
        3. Save costs by paying only for the compu''',
     'referencia': 'https://aws.amazon.com/lambda/'},
    {'pregunta': 'Which AWS service or feature allows users to connect with and deploy AWS services programmatically?',
     'opciones': '''A. AWS Management Console. 
B. AWS Cloud9. 
C. AWS CodePipeline. 
D. AWS software development kits (SDKs)''',
     'respuesta': 'AWS software development kits (SDKs)',
     'argumento': 'AWS software development kits (SDKs) allow users to connect with and deploy AWS services programmatically, using programming languages such as Java, Python, .NET, and more. The AWS SDKs provide APIs that abstract low-level interactions with the services and allow developers to manage AWS services and resources from within their own applications. The AWS SDKs are available for multiple programming languages and platforms.',
     'referencia': 'https://docs.aws.amazon.com/sdk-for-java/?icmpid=docs_homepage_sdktoolkits'},
    {'pregunta': 'A company plans to create a data lake that uses Amazon S3. Which factor will have the MOST effect on cost?',
     'opciones': '''A. The selection of S3 storage tiers. 
B. Charges to transfer existing data into Amazon S3.
C. The addition of S3 bucket policies. 
D. S3 ingest fees for each request''',
     'respuesta': 'The selection of S3 storage tiers',
     'argumento': 'The storage class used in Amazon S3 can certainly have an impact on the cost of a data lake, as different storage classes have different pricing tiers. For example, using the Glacier storage class for infrequently accessed data can be much cheaper than using the Standard storage class for frequently accessed data. However, in most cases, the amount of data stored will have a larger impact on the overall cost than the storage class used. This is because storage usage is generally the primary driver of cost in an S3-based data lake, regardless of the storage class. Therefore, it is important to carefully monitor and manage the amount of data being stored in the S3 bucket to keep costs under control.',
     'referencia': 'https://aws.amazon.com/s3/pricing/'},
    {'pregunta': 'A company is launching an ecommerce application that must always be available. The application will run on Amazon EC2 instances continuously for the next 12 months. What is the MOST cost-effective instance purchasing option that meets these requirements?',
     'opciones': '''A. Spot Instances.
B. Savings Plans.
C. Dedicated Hosts.
D. On-Demand Instances''',
     'respuesta': 'Savings Plans',
     'argumento': 'Amazon EC2 Savings Plans enable you to reduce your compute costs by committing to a consistent amount of compute usage for a 1-year or 3-year term. This results in savings of up to 72% over On-Demand Instance costs. Any usage up to the commitment is charged at the discounted Savings Plan rate (for example, $10 an hour). Any usage beyond the commitment is charged at regular On-Demand Instance rates.',
     'referencia': 'https://aws.amazon.com/savingsplans/'}, #15
    {'pregunta': 'Which AWS service or feature can a company use to determine which business unit is using specific AWS resources?',
     'opciones': '''A. Cost allocation tags.
B. Key pairs.
C. Amazon Inspector.
D. AWS Trusted Advisor''',
     'respuesta': 'Cost allocation tags',
     'argumento': 'Cost allocation tags are a mechanism provided by AWS to assign metadata to AWS resources for cost tracking and categorization purposes. By applying cost allocation tags to resources, companies can associate custom metadata to identify and categorize resources based on different criteria, such as business unit, department, project, or application. When using cost allocation tags, companies can track and analyze their AWS costs based on the assigned tags. This allows them to determine the cost distribution among different business units or any other relevant categorization. Cost allocation tags provide granular visibility into resource usage and expenditure, enabling accurate cost attribution and analysis.',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html'},
    {'pregunta': 'A company wants to migrate its workloads to AWS, but it lacks expertise in AWS Cloud computing. Which AWS service or feature will help the company with its migration?',
     'opciones': '''A. AWS Trusted Advisor.
B. AWS Consulting Partners.
C. AWS Artifacts.
D. AWS Managed Services''',
     'respuesta': 'AWS Managed Services',
     'argumento': 'AWS Managed Services is a service offered by AWS that helps organizations migrate their workloads to the AWS cloud. It provides comprehensive management of AWS infrastructure and automates common tasks, allowing the company to focus on its core business rather than worrying about the complexities of managing the cloud environment. With AWS Managed Services, the company can benefit from AWS-certified experts who will handle the day-to-day management of its AWS infrastructure. This includes activities such as provisioning, monitoring, patching, backup, and security. The service ensures that best practices are followed and that the company´s workloads are optimized for performance, cost, and security. By leveraging AWS Managed Services, the company can overcome its lack of expertise in AWS cloud computing and have a smooth migration to the AWS platform.',
     'referencia': 'https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html'},
    {'pregunta': 'Which AWS service or tool should a company use to centrally request and track service limit increases?',
     'opciones': '''A. AWS Config.
B. Service Quotas.
C. AWS Service Catalog.
D. AWS Budgets''',
     'respuesta': 'Service Quotas',
     'argumento': 'Service Quotas is an AWS service that allows users to view, manage, and request increases in service limits for various AWS services. Service limits are predefined limits set by AWS on the usage of specific resources or services within an AWS account. By using Service Quotas, a company can centrally manage its service limits and request increases when needed. It provides visibility into the current limits, usage, and available quota for each service. The service includes an interface to submit requests for limit increases, track the status of the requests, and receive notifications on updates.',
     'referencia': 'https://aws.amazon.com/about-aws/whats-new/2021/04/service-quotas-available-aws-govcloud-us-regions/'},
    {'pregunta': 'Which documentation does AWS Artifact provide?',
     'opciones': '''A. Amazon EC2 terms and conditions.
B. AWS ISO certifications.
C. A history of a company´s AWS spending.
D. A list of previous-generation Amazon EC2 instance types''',
     'respuesta': 'AWS ISO certifications',
     'argumento': 'AWS Artifact provides access to various compliance-related documents, including AWS ISO certifications. ISO certifications are international standards that define best practices for information security management systems. Through AWS Artifact, customers can access AWS´s ISO certifications, such as ISO 27001, which specifies requirements for establishing, implementing, maintaining, and continuously improving an information security management system within the context of AWS services.',
     'referencia': 'https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html'},
    {'pregunta': 'Which task requires using AWS account root user credentials?',
     'opciones': '''A. Viewing billing information.
B. Changing the AWS Support plan.
C. Starting and stopping Amazon EC2 instances.
D. Opening an AWS Support case''',
     'respuesta': 'Changing the AWS Support plan',
     'argumento': 'Changing the AWS Support plan, which includes upgrading or downgrading the level of support, typically requires the privileges associated with the AWS account root user. The root user has full access and permissions to manage all aspects of the AWS account, including billing and support-related configurations.',
     'referencia': 'https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html'}, #20
    {'pregunta': 'A company needs to simultaneously process hundreds of requests from different users. Which combination of AWS services should the company use to build an operationally efficient solution?',
     'opciones': '''A. Amazon Simple Queue Service (Amazon SQS) and AWS Lambda.
B. AWS Data Pipeline and Amazon EC2.
C. Amazon Kinesis and Amazon Athena.
D. AWS Amplify and AWS AppSync''',
     'respuesta': 'Amazon Simple Queue Service (Amazon SQS) and AWS Lambda',
     'argumento': '''The combination of SQS and Lambda offers several benefits:
                     Scalability: SQS allows for handling a large number of requests, while Lambda automatically scales the processing capacity based on the incoming workload.
                     Reliability: SQS ensures reliable message delivery, and Lambda functions are designed to be stateless and fault-tolerant.
                     Decoupling: The decoupling of services through SQS enables loose coupling, allowing components to evolve independently and scale separately.''',
     'referencia': ''},
    {'pregunta': 'What is the scope of a VPC within the AWS network?',
     'opciones': '''A. A VPC can span all Availability Zones globally. 
B. A VPC must span at least two subnets in each AWS Region. 
C. A VPC must span at least two edge locations in each AWS Region. 
D. A VPC can span all Availability Zones within an AWS Region.''',
     'respuesta': 'A VPC can span all Availability Zones within an AWS Region.',
     'argumento': 'A VPC is a logically isolated section of the AWS cloud where users can launch resources such as Amazon EC2 instances, Amazon RDS databases, and other AWS services. It provides control over networking aspects, including IP addressing, subnets, routing tables, and network gateways. When creating a VPC, users can choose the AWS Region where it will reside. Within that Region, a VPC can span multiple Availability Zones. Availability Zones are separate data centers within a given Region, each with redundant power, networking, and connectivity. By spanning multiple Availability Zones, a VPC can provide high availability and fault tolerance for resources deployed within it.',
     'referencia': ''},
    {'pregunta': 'Which of the following are components of an AWS Site-to-Site VPN connection? (Choose two.)',
     'opciones': '''A. AWS Storage Gateway. 
B. Virtual private gateway. 
C. NAT gateway. 
D. Customer gateway. 
E. Internet gateway.''',
     'respuesta': '''B. Virtual private gateway. 
D. Customer gateway.''',
     'argumento': 'Virtual private gateway: A virtual private gateway is the AWS side of the VPN connection. It serves as the entry point for traffic from the customer network into the AWS network. Customer gateway: A customer gateway is the customer´s side of the VPN connection. It represents the physical device or software application located in the customer´s on-premises network.',
     'referencia': 'https://docs.aws.amazon.com/vpn/latest/s2svpn/Examples.html'},
    {'pregunta': 'A company needs to establish a connection between two VPCs. The VPCs are located in two different AWS Regions. The company wants to use the existing infrastructure of the VPCs for this connection. Which AWS service or feature can be used to establish this connection?',
     'opciones': '''A. AWS Client VPN. 
B. VPC peering. 
C. AWS Direct Connect. 
D. VPC endpoints.''',
     'respuesta': 'VPC peering',
     'argumento': 'You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html'},
    {'pregunta': 'According to the AWS shared responsibility model, what responsibility does a customer have when using Amazon RDS to host a database?',
     'opciones': '''A. Manage connections to the database. 
B. Install Microsoft SQL Server. 
C. Design encryption-at-rest strategies. 
D. Apply minor database patches.''',
     'respuesta': 'Manage connections to the database.',
     'argumento': 'Amazon RDS encrypts your databases using keys you manage with the AWS Key Management Service (KMS). On a database instance running with Amazon RDS encryption, data stored at rest in the underlying storage is encrypted, as are its automated backups, read replicas, and snapshots. Amazon RDS encryption uses the industry standard AES-256 encryption algorithm to encrypt your data on the server that hosts your Amazon RDS instance. Designing an encryption strategy means building the strategy from scratch (including choosing the best-fit encryption algorithm for that strategy), as mentioned before, selecting a one is different from design/create a new one.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html'}, #25
    {'pregunta': 'What are some advantages of using Amazon EC2 instances to host applications in the AWS Cloud instead of on premises? (Choose two.)',
     'opciones': '''A. EC2 includes operating system patch management. 
B. EC2 integrates with Amazon VPC, AWS CloudTrail, and AWS Identity and Access Management (IAM). 
C. EC2 has a 100% service level agreement (SLA). 
D. EC2 has a flexible, pay-as-you-go pricing model.''',
     'respuesta': 'EC2 has a flexible, pay-as-you-go pricing model. EC2 has automatic storage cost optimization.',
     'argumento': '',
     'referencia': 'https://aws.amazon.com/ec2/instance-types/'},
    {'pregunta': 'A user needs to determine whether an Amazon EC2 instance´s security groups were modified in the last month. How can the user see if a change was made?',
     'opciones': '''A. Use Amazon EC2 to see if the security group was changed. 
B. Use AWS Identity and Access Management (IAM) to see which user or role changed the security group. 
C. Use AWS CloudTrail to see if the security group was changed. 
D. Use Amazon CloudWatch to see if the security group was changed.''',
     'respuesta': 'Use AWS CloudTrail to see if the security group was changed.',
     'argumento': 'CloudTrail records user activity and API calls across AWS services as events. CloudTrail events help you answer the questions of "who did what, where, and when?',
     'referencia': 'https://aws.amazon.com/cloudtrail/features/'},
    {'pregunta': 'Which AWS service will help protect applications running on AWS from DDoS attacks?',
     'opciones': '''A. Amazon GuardDuty. 
B. AWS WAF. 
C. AWS Shield. 
D. Amazon Inspector.''',
     'respuesta': 'AWS Shield.',
     'argumento': 'AWS Shield is a managed service that provides protection against Distributed Denial of Service (DDoS) attacks for applications running on AWS. AWS Shield Standard is automatically enabled to all AWS customers at no additional cost. AWS Shield Advanced is an optional paid service. AWS Shield Advanced provides additional protections against more sophisticated and larger attacks for your applications running on Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Route 53',
     'referencia': 'https://aws.amazon.com/shield/faqs/'},
    {'pregunta': 'Which AWS service or feature acts as a firewall for Amazon EC2 instances?',
     'opciones': '''A. Network ACL. 
B. Elastic network interface. 
C. Amazon VPC. 
D. Security group''',
     'respuesta': 'Security group',
     'argumento': 'A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html'},
    {'pregunta': 'How does the AWS Cloud pricing model differ from the traditional on-premises storage pricing model?',
     'opciones': '''A. AWS resources do not incur costs. 
B. There are no infrastructure operating costs. 
C. There are no upfront cost commitments. 
D. There are no software licensing costs.''',
     'respuesta': 'There are no infrastructure operating costs.',
     'argumento': 'Reduce storage spend Minimize your total cost of ownership (TCO) with managed services that eliminate infrastructure maintenance. Optimize your storage costs based on how frequently and quickly you need to access your data.',
     'referencia': 'https://aws.amazon.com/products/storage/'}, #30
    {'pregunta': 'A company has a single Amazon EC2 instance. The company wants to adopt a highly available architecture. What can the company do to meet this requirement?',
     'opciones': '''A. Scale vertically to a larger EC2 instance size. 
B. Scale horizontally across multiple Availability Zones. 
C. Purchase an EC2 Dedicated Instance. 
D. Change the EC2 instance family to a compute optimized instance.''',
     'respuesta': 'Scale horizontally across multiple Availability Zones.',
     'argumento': 'There are two types of Scaling: Vertical & Horizontal. Vertical: Means increasing the configuration of the same existing machine.  Horizontal: Adding additional instances to share the work load, so answer her should be B',
     'referencia': ''},
    {'pregunta': 'A company´s on-premises application deployment cycle was 3-4 weeks. After migrating to the AWS Cloud, the company can deploy the application in 2-3 days. Which benefit has this company experienced by moving to the AWS Cloud?',
     'opciones': '''A. Elasticity. 
B. Flexibility. 
C. Agility. 
D. Resilience''',
     'respuesta': 'Agility.',
     'argumento': 'The company can quickly respond to business needs and deploy applications faster, allowing for faster time-to-market for new features, updates, or bug fixes. This increased agility enables the company to stay competitive in a rapidly changing market.',
     'referencia': 'https://repost.aws/questions/QU89MN7WVwTcCsNELreRby8A/agility-or-elasticity'},
    {'pregunta': 'Which of the following are included in AWS Enterprise Support? (Choose two.)',
     'opciones': '''A. AWS technical account manager (TAM). 
B. AWS partner-led support. 
C. AWS Professional Services. 
D. Support of third-party software integration to AWS. 
E. 5-minute response time for critical issues''',
     'respuesta': '''A. AWS technical account manager (TAM). 
D. Support of third-party software integration to AWS.''',
     'argumento': 'With Enterprise level support you get: Third-party software support for guidance, configuration, and troubleshooting of AWS interoperability with many common OSs, platforms, and app stack components. You will also get access to a Technical Account Manager (TAM) who will provide consultative architectural and operational guidance delivered in the context of your apps and use-cases to help you achieve the greatest value from AWS.',
     'referencia': 'https://i.ytimg.com/vi/0LQcq_zyNmg/maxresdefault.jpg, https://aws.amazon.com/premiumsupport/plans/enterprise/'},
    {'pregunta': 'A global media company uses AWS Organizations to manage multiple AWS accounts. Which AWS service or feature can the company use to limit the access to AWS services for member accounts?',
     'opciones': '''A. AWS Identity and Access Management (IAM). 
B. Service control policies (SCPs). 
C. Organizational units (OUs). 
D. Access control lists (ACLs)''',
     'respuesta': 'Service control policies (SCPs).',
     'argumento': 'AWS Organizations helps to manage multiple AWS accounts in a centralized manner. SCPs are a feature of AWS Organizations that allow an organization to set rules that govern the use of AWS services across all accounts in the organization. SCPs can be used to restrict the use of specific AWS services or to impose additional conditions or requirements on the use of those services. SCPs are applied at the organizational unit (OU) level, so organizations can create different policies for different groups of accounts within their AWS Organization.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html#:~:text=.%20In%20SCPs%2C%20you,in%20the%20organization.'},
    {'pregunta': 'A company wants to limit its employees AWS access to a portfolio of predefined AWS resources. Which AWS solution should the company use to meet this requirement?',
     'opciones': '''A. AWS Config. 
B. AWS software development kits (SDKs). 
C. AWS Service Catalog. 
D. AWS AppSync''',
     'respuesta': 'AWS Service Catalog.',
     'argumento': 'AWS Service Catalog can create, organize, and govern a curated catalog of AWS resources that can be shared at the permissions level so you can quickly provision approved cloud resources without needing direct access to the underlying AWS services.',
     'referencia': 'https://aws.amazon.com/servicecatalog/#:~:text=AWS%20Service%20Catalog%3F,the%20underlying%20AWS%20services.'}, #35
    {'pregunta': 'An online company was running a workload on premises and was struggling to launch new products and features. After migrating the workload to AWS, the company can quickly launch products and features and can scale its infrastructure as required. Which AWS Cloud value proposition does this scenario describe?',
     'opciones': '''A. Business agility. 
B. High availability. 
C. Security. 
D. Centralized auditing.''',
     'respuesta': 'Business agility.',
     'argumento': 'Increase speed and agility – In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which of the following are advantages of the AWS Cloud? (Choose two.)',
     'opciones': '''A. AWS management of user-owned infrastructure. 
B. Ability to quickly change required capacity. 
C. High economies of scale. 
D. Increased deployment time to market. 
E. Increased fixed expenses''',
     'respuesta': '''B. Ability to quickly change required capacity. 
C. High economies of scale.''',
     'argumento': 'Economy at scale: You profit of massive aggregation of resources consumed by all customers on the AWS platform. Rapidity and Agility.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'AWS has the ability to achieve lower pay-as-you-go pricing by aggregating usage across hundreds of thousands of users. This describes which advantage of the AWS Cloud?',
     'opciones': '''A. Launch globally in minutes. 
B. Increase speed and agility. 
C. High economies of scale. 
D. No guessing about compute capacity''',
     'respuesta': 'High economies of scale.',
     'argumento': 'Benefit from massive economies of scale – By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html#:~:text=Benefit%20from%20massive,you%2Dgo%20prices.'},
    {'pregunta': 'A company has a database server that is always running. The company hosts the server on Amazon EC2 instances. The instance sizes are suitable for the workload. The workload will run for 1 year. Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?',
     'opciones': '''A. Standard Reserved Instances. 
B. On-Demand Instances. 
C. Spot Instances. 
D. Convertible Reserved Instances''',
     'respuesta': 'Standard Reserved Instances.',
     'argumento': 'Standard Reserved Instances provide you with a significant discount (up to 72%) compared to On-Demand Instance pricing, and can be purchased for a 1-year or 3-year term. Customers have the flexibility to change the Availability Zone, the instance size, and networking type of their Standard Reserved Instances. Purchase Convertible Reserved Instances if you need additional flexibility, such as the ability to use different instance families, operating systems, or tenancies over the Reserved Instance term. Convertible Reserved Instances provide you with a significant discount (up to 66%) compared to On-Demand Instances and can be purchased for a 1-year or 3-year term.',
     'referencia': 'https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/'},
    {'pregunta': 'A company is developing a mobile app that needs a high-performance NoSQL database. Which AWS services could the company use for this database? (Choose two.)',
     'opciones': '''A. Amazon Aurora. 
B. Amazon RDS. 
C. Amazon Redshift. 
D. Amazon DocumentDB (with MongoDB compatibility). 
E. Amazon DynamoDB''',
     'respuesta': '''D. Amazon DocumentDB (with MongoDB compatibility). 
E. Amazon DynamoDB.''',
     'argumento': 'Amazon DynamoDB, which is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Amazon DocumentDB (with MongoDB compatibility), which is a fully managed document database service that supports MongoDB workloads and provides high performance, scalability, and availability with the security and compliance capabilities of AWS.',
     'referencia': 'https://aws.amazon.com/nosql/'}, #40
    {'pregunta': 'Which tasks are the responsibility of AWS, according to the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Patch the Amazon EC2 guest operating system. 
B. Upgrade the firmware of the network infrastructure. 
C. Apply password rotation for IAM users. 
D. Maintain the physical security of edge locations. 
E. Maintain least privilege access to the root user account.''',
     'respuesta': '''B. Upgrade the firmware of the network infrastructure. 
     D. Maintain the physical security of edge locations.''',
     'argumento': 'Upgrade the firmware of the network infrastructure: AWS is responsible for managing and maintaining the underlying network infrastructure, including upgrading the firmware of their network devices and equipment. Maintain the physical security of edge locations: AWS is responsible for the physical security of its global infrastructure, which includes the security and protection of edge locations.',
     'referencia': 'As shown in https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'Which of the following are features of network ACLs as they are used in the AWS Cloud? (Choose two.)',
     'opciones': '''A. They are stateless. 
B. They are stateful. 
C. They evaluate all rules before allowing traffic. 
D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic. 
E. They operate at the instance level.''',
     'respuesta': '''A. They are stateless. 
D. They process rules in order, starting with the lowest numbered rule, when deciding whether to allow traffic.''',
     'argumento': 'They are stateless: Network ACLs in AWS are stateless, meaning they do not keep track of the state of a connection. Each incoming and outgoing packet is evaluated independently based on the rules defined in the ACL. They process rules in order, starting with the lowest numbered rule when deciding whether to allow traffic: Network ACLs evaluate rules sequentially and process them in order, starting with the lowest numbered rule. Once a matching rule is found, processing stops, and the decision to allow or deny traffic is made based on that rule. No further rules are evaluated.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html'},
    {'pregunta': 'A company has designed its AWS Cloud infrastructure to run its workloads effectively. The company also has protocols in place to continuously improve supporting processes. Which pillar of the AWS Well-Architected Framework does this scenario represent?',
     'opciones': '''A. Security. 
B. Performance efficiency. 
C. Cost optimization. 
D. Operational excellence''',
     'respuesta': 'Operational excellence',
     'argumento': 'Operational excellence in the AWS Well-Architected Framework refers to the ability to run and monitor systems effectively, continuously improving processes and procedures. It encompasses designing and managing workloads to achieve business and customer goals efficiently. It focuses on automating processes, identifying areas for improvement, and making informed decisions based on operational data and feedback.',
     'referencia': 'https://wa.aws.amazon.com/wat.pillars.wa-pillars.en.html'},
    {'pregunta': 'A company needs to graphically visualize AWS billing and usage over time. The company also needs information about its AWS monthly costs. Which AWS Billing and Cost Management tool provides this data in a graphical format?',
     'opciones': '''A. AWS Bills. 
B. Cost Explorer. 
C. AWS Cost and Usage Report. 
D. AWS Budgets''',
     'respuesta': 'Cost Explorer.',
     'argumento': 'Cost Explorer (B) enables users to visualize and understand their AWS costs and usage trends over time. It also provides information about the monthly costs of AWS services and allows users to create custom cost reports and budgets. The other options, AWS Bills, AWS Cost and Usage Report, and AWS Budgets provide different functionalities related to billing and cost management in AWS, but they do not provide graphical visualization of data.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'},
    {'pregunta': 'Which AWS service or feature can be used to create a private connection between an on-premises workload and an AWS Cloud workload?',
     'opciones': '''A. Amazon Route 53. 
B. Amazon Macie. 
C. AWS Direct Connect. 
D. AWS PrivateLink''',
     'respuesta': 'AWS PrivateLink',
     'argumento': 'AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), supported AWS services, and your on-premises networks without exposing your traffic to the public internet.',
     'referencia': 'https://d1.awsstatic.com/products/privatelink/product-page-diagram_AWS-PrivateLink.fc899b8ebd46fa0b3537d9be5b2e82de328c63b8.png, https://aws.amazon.com/privatelink/#:~:text=AWS%20PrivateLink%20provides%20private%20connectivity,traffic%20to%20the%20public%20internet'}, #45
    {'pregunta': 'A company wants to run production workloads on AWS. The company needs concierge service, a designated AWS technical account manager (TAM), and technical support that is available 24 hours a day, 7 days a week. Which AWS Support plan will meet these requirements?',
     'opciones': '''A. AWS Basic Support. 
B. AWS Enterprise Support. 
C. AWS Business Support. 
D. AWS Developer Support''',
     'respuesta': 'AWS Enterprise Support.',
     'argumento': 'AWS Enterprise Support is the highest level of support offered by AWS and provides access to a range of benefits and services, including a dedicated technical account manager (TAM). The TAM serves as a single point of contact, providing personalized guidance and assistance in utilizing AWS services effectively, optimizing workloads, and addressing technical inquiries or issues. In addition to the TAM, AWS Enterprise Support offers concierge service, which provides assistance with billing and account-related inquiries, service limit increases, and general operational support. AWS Enterprise Support also includes 24/7 technical support, ensuring that assistance is available around the clock for critical issues or emergencies.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/enterprise/'},
    {'pregunta': 'Which architecture design principle describes the need to isolate failures between dependent components in the AWS Cloud?',
     'opciones': '''A. Use a monolithic design. 
B. Design for automation. 
C. Design for single points of failure. 
D. Loosely couple components.''',
     'respuesta': 'Loosely couple components.',
     'argumento': 'Loose coupling is a design principle that emphasizes reducing dependencies between components in a system. In the context of the AWS Cloud, it means designing systems where components can function independently, with minimal reliance on other components. By loosely coupling components, failures in one component are isolated and do not propagate to other components. This approach enhances the overall fault tolerance and resilience of the system. If one component fails, it does not bring down or impact other components, allowing the system to continue functioning or degrade gracefully. Loose coupling is achieved by using well-defined interfaces, decoupling communication mechanisms, and employing distributed system patterns such as message queues, event-driven architectures, and microservices.',
     'referencia': ''},
    {'pregunta': 'Which AWS services are managed database services? (Choose two.)',
     'opciones': '''A. Amazon Elastic Block Store (Amazon EBS). 
B. Amazon S3. 
C. Amazon RDS. 
D. Amazon Elastic File System (Amazon EFS). 
E. Amazon DynamoDB''',
     'respuesta': '''B. Amazon RDS. 
C. Amazon DynamoDB.''',
     'argumento': 'Amazon RDS: Amazon RDS (Relational Database Service) is a fully managed database service that supports popular relational database engines such as MySQL, PostgreSQL, Oracle, SQL Server, and Amazon Aurora. It handles administrative tasks such as database setup, patching, backups, and automated backups, allowing users to focus on their applications rather than database management. Amazon DynamoDB: Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It offers automatic scaling, built-in security, and automated backups, making it an ideal choice for applications that require low-latency data access and flexible scaling.',
     'referencia': ''},
    {'pregunta': 'A company is using the AWS Free Tier for several AWS services for an application. What will happen if the Free Tier usage period expires or if the application use exceeds the Free Tier usage limits?',
     'opciones': '''A. The company will be charged the standard pay-as-you-go service rates for the usage that exceeds the Free Tier usage. 
B. AWS Support will contact the company to set up standard service charges. 
C. The company will be charged for the services it consumed during the Free Tier period, plus additional charges for service consumption after the Free Tier period. 
D. The company´s AWS account will be frozen and can be restarted after a payment plan is established.''',
     'respuesta': 'The company will be charged the standard pay-as-you-go service rates for the usage that exceeds the Free Tier usage.',
     'argumento': 'When the Free Tier usage period ends or the application exceeds the Free Tier limits, the company will start incurring charges for the services used beyond the Free Tier allowances. These charges will be based on the standard pay-as-you-go rates for each AWS service that is being utilized.',
     'referencia': 'https://aws.amazon.com/free/free-tier-faqs/?audit=2019q1'},
    {'pregunta': 'A company recently deployed an Amazon RDS instance in its VPC. The company needs to implement a stateful firewall to limit traffic to the private corporate network. Which AWS service or feature should the company use to limit network traffic directly to its RDS instance?',
     'opciones': '''A. Network ACLs.
B. Security groups. 
C. AWS WAF. 
D. Amazon GuardDuty''',
     'respuesta': 'Security groups.',
     'argumento': 'VPC security groups control the access that traffic has in and out of a DB instance. By default, network access is turned off for a DB instance. You can specify rules in a security group that allow access from an IP address range, port, or security group.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules.html'}, #50
    {'pregunta': 'Which AWS service uses machine learning to help discover, monitor, and protect sensitive data that is stored in Amazon S3 buckets?',
     'opciones': '''A. AWS Shield. 
B. Amazon Macie. 
C. AWS Network Firewall. 
D. Amazon Cognito''',
     'respuesta': 'Amazon Macie.',
     'argumento': 'Amazon Macie is a security service offered by AWS that leverages machine learning algorithms to automatically discover, classify, and protect sensitive data stored in Amazon S3 buckets. It helps organizations identify and understand the content of their S3 data by analyzing the data for sensitive information such as personally identifiable information (PII), financial data, and intellectual property. Macie uses machine learning models to identify and classify data patterns, enabling the detection of sensitive data even if it is stored in an unstructured format or embedded within larger files. It provides automated alerts and generates reports to assist with data privacy and compliance efforts.',
     'referencia': 'https://aws.amazon.com/macie/'},
    {'pregunta': 'A company wants to improve the overall availability and performance of its applications that are hosted on AWS. Which AWS service should the company use?',
     'opciones': '''A. Amazon Connect. 
B. Amazon Lightsail. 
C. AWS Global Accelerator. 
D. AWS Storage Gateway''',
     'respuesta': 'AWS Global Accelerator',
     'argumento': 'AWS Global Accelerator is a networking service that improves the performance of your users’ traffic by up to 60% using Amazon Web Services’ global network infrastructure. When the internet is congested, AWS Global Accelerator optimizes the path to your application to keep packet loss, jitter, and latency consistently low.',
     'referencia': 'https://aws.amazon.com/global-accelerator/?blogs-global-accelerator.sort-by=item.additionalFields.createdDate&blogs-global-accelerator.sort-order=desc&aws-global-accelerator-wn.sort-by=item.additionalFields.postDateTime&aws-global-accelerator-wn.sort-order=desc'},
    {'pregunta': 'Which AWS service or feature identifies whether an Amazon S3 bucket or an IAM role has been shared with an external entity?',
     'opciones': '''A. AWS Service Catalog. 
B. AWS Systems Manager. 
C. AWS IAM Access Analyzer. 
D. AWS Organizations''',
     'respuesta': 'AWS IAM Access Analyze',
     'argumento': 'Access Analyzer helps you identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, shared with an external entity. This lets you identify unintended access to your resources and data, which is a security risk.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html'},
    {'pregunta': 'A company does not want to rely on elaborate forecasting to determine its usage of compute resources. Instead, the company wants to pay only for the resources that it uses. The company also needs the ability to increase or decrease its resource usage to meet business requirements. Which pillar of the AWS Well-Architected Framework aligns with these requirements?',
     'opciones': '''A. Operational excellence. 
B. Security. 
C. Reliability. 
D. Cost optimization''',
     'respuesta': 'Cost optimization',
     'argumento': 'The requirements mentioned align with the "Cost Optimization" pillar of the AWS Well-Architected Framework. This pillar focuses on designing systems that deliver business value at the lowest possible price point, by optimizing costs in multiple dimensions such as elasticity, expenditure awareness, and resource utilization. By paying only for the resources that it uses and having the ability to increase or decrease resource usage, the company can achieve cost optimization.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/design-principles-4.html'},
    {'pregunta': 'A company wants to launch its workload on AWS and requires the system to automatically recover from failure. Which pillar of the AWS Well-Architected Framework includes this requirement?',
     'opciones': '''A. Cost optimization. 
B. Operational excellence. 
C. Performance efficiency. 
D. Reliability''',
     'respuesta': 'Reliability',
     'argumento': 'The reliability pillar includes the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/reliability-pillar.html'}, #55
    {'pregunta': 'A large enterprise with multiple VPCs in several AWS Regions around the world needs to connect and centrally manage network connectivity between its VPCs. Which AWS service or feature meets these requirements?',
     'opciones': '''A. AWS Direct Connect. 
B. AWS Transit Gateway. 
C. AWS Site-to-Site VPN. 
D. VPC endpoints''',
     'respuesta': 'AWS Transit Gateway.',
     'argumento': 'AWS Transit Gateway is a fully managed service that simplifies the connectivity and routing between VPCs and on-premises networks. It acts as a hub that enables inter-VPC communication and connectivity to on-premises data centers or remote networks. With AWS Transit Gateway, the large enterprise can create a single gateway and establish peering connections with multiple VPCs across different AWS Regions. This allows for centralized management and control of network traffic between VPCs, simplifying network architecture and reducing administrative overhead.',
     'referencia': 'https://aws.amazon.com/transit-gateway/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc'},
    {'pregunta': 'Which AWS service supports the creation of visual reports from AWS Cost and Usage Report data?',
     'opciones': '''A. Amazon Athena. 
B. Amazon QuickSight. 
C. Amazon CloudWatch. 
D. AWS Organizations''',
     'respuesta': 'Amazon QuickSight.',
     'argumento': 'Amazon QuickSight is a business intelligence (BI) service that allows users to create interactive visualizations, reports, and dashboards from various data sources, including AWS services. It provides rich visualization capabilities to analyze and explore data, enabling users to gain insights and make data-driven decisions. With Amazon QuickSight, users can connect to their AWS Cost and Usage Report data and create visual reports to analyze and track their AWS costs. They can build charts, graphs, and other visualizations to understand cost trends, identify cost drivers, and compare spending across different dimensions such as services, accounts, regions, and more.',
     'referencia': 'https://aws.amazon.com/premiumsupport/knowledge-center/quicksight-cost-usage-report/'},
    {'pregunta': 'Which AWS service should be used to monitor Amazon EC2 instances for CPU and network utilization?',
     'opciones': '''A. Amazon Inspector. 
B. AWS CloudTrail. 
C. Amazon CloudWatch. 
D. AWS Config''',
     'respuesta': 'Amazon CloudWatch',
     'argumento': 'Amazon CloudWatch is a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics. CloudWatch uses metrics to represent the data points for your resources. AWS services send metrics to CloudWatch. CloudWatch then uses these metrics to create graphs automatically that show how performance has changed over time.',
     'referencia': ''},
    {'pregunta': 'A company is preparing to launch a new web store that is expected to receive high traffic for an upcoming event. The web store runs only on AWS, and the company has an AWS Enterprise Support plan. Which AWS resource will provide guidance about how the company should scale its architecture and operational support during the event?',
     'opciones': '''A. AWS Abuse team. 
B. The designated AWS technical account manager (TAM). 
C. AWS infrastructure event management. 
D. AWS Professional Services''',
     'respuesta': 'The designated AWS technical account manager (TAM)',
     'argumento': 'In this scenario, the designated AWS technical account manager (TAM) will provide guidance about how the company should scale its architecture and operational support during the event. A TAM is a resource available to customers with an AWS Enterprise Support plan. They act as a trusted advisor and provide personalized support and guidance to help customers achieve their business goals and effectively utilize AWS services.',
     'referencia': 'https://aws.amazon.com/premiumsupport/programs/iem/'},
    {'pregunta': 'A user wants to deploy a service to the AWS Cloud by using infrastructure-as-code (IaC) principles. Which AWS service can be used to meet this requirement?',
     'opciones': '''A. AWS Systems Manager. 
B. AWS CloudFormation. 
C. AWS CodeCommit. 
D. AWS Config''',
     'respuesta': 'AWS CloudFormation.',
     'argumento': 'AWS CloudFormation is designed to allow resource lifecycles to be managed repeatably, predictable, and safely, while allowing for automatic rollbacks, automated state management, and management of resources across accounts and regions',
     'referencia': 'https://aws.amazon.com/cloudformation/faqs/'}, #60
    {'pregunta': 'A company that has multiple business units wants to centrally manage and govern its AWS Cloud environments. The company wants to automate the creation of AWS accounts, apply service control policies (SCPs), and simplify billing processes. Which AWS service or tool should the company use to meet these requirements?',
     'opciones': '''A. AWS Organizations. 
B. Cost Explorer. 
C. AWS Budgets. 
D. AWS Trusted Advisor''',
     'respuesta': 'AWS Organizations.',
     'argumento': 'AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html'},
    {'pregunta': 'Which IT controls do AWS and the customer share, according to the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Physical and environmental controls. 
B. Patch management. 
C. Cloud awareness and training. 
D. Zone security. 
E. Application data encryption''',
     'respuesta': '''B. Patch management. 
C. Cloud awareness and training.''',
     'argumento': 'Physical and environmental controls: AWS is responsible for ensuring the security and protection of the physical infrastructure of their data centers, including measures like access controls, surveillance, and environmental safeguards. However, customers also play a role in implementing physical and environmental controls within their own premises or within their applications running on AWS. Patch management: AWS is responsible for patching and securing the underlying infrastructure and host operating system. However, customers are responsible for managing the patches and updates for their own applications, virtual machines, or containers running on the AWS infrastructure',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'A company is launching an application in the AWS Cloud. The application will use Amazon S3 storage. A large team of researchers will have shared access to the data. The company must be able to recover data that is accidentally overwritten or deleted. Which S3 feature should the company turn on to meet this requirement?',
     'opciones': '''A. Server access logging. 
B. S3 Versioning. 
C. S3 Lifecycle rules. 
D. Encryption in transit and at rest''',
     'respuesta': 'S3 Versioning',
     'argumento': 'Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket. You can use the S3 Versioning feature to preserve, retrieve, and restore every version of every object stored in your buckets. With versioning you can recover more easily from both unintended user actions and application failures.',
     'referencia': 'https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html'},
    {'pregunta': 'A manufacturing company has a critical application that runs at a remote site that has a slow internet connection. The company wants to migrate the workload to AWS. The application is sensitive to latency and interruptions in connectivity. The company wants a solution that can host this application with minimum latency. Which AWS service or feature should the company use to meet these requirements?',
     'opciones': '''A. Availability Zones. 
B. AWS Local Zones. 
C. AWS Wavelength. 
D. AWS Outposts''',
     'respuesta': 'AWS Local Zones',
     'argumento': 'Run applications that require single-digit millisecond latency or local data processing by bringing AWS infrastructure closer to your end users and business centers.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/localzones/'},
    {'pregunta': 'A company wants to migrate its applications from its on-premises data center to a VPC in the AWS Cloud. These applications will need to access on-premises resources. Which actions will meet these requirements? (Choose two.)',
     'opciones': '''A. Use AWS Service Catalog to identify a list of on-premises resources that can be migrated. 
B. Create a VPN connection between an on-premises device and a virtual private gateway in the VPC. 
C. Use an Amazon CloudFront distribution and configure it to accelerate content delivery close to the on-premises resources. 
D. Set up an AWS Direct Connect connection between the on-premises data center and AWS. 
E. Use Amazon CloudFront to restrict access to static web content provided through the on-premises web servers.''',
     'respuesta': '''A. Use AWS Service Catalog to identify a list of on-premises resources that can be migrated. 
D. Set up an AWS Direct Connect connection between the on-premises data center and AWS.''',
     'argumento': 'in the scenario requieres 2 main objectives. (1) migrate its applications and (2) access on-premises resources, option A meets the first and D the second',
     'referencia': ''}, #65
    {'pregunta': 'A company wants to use the AWS Cloud to provide secure access to desktop applications that are running in a fully managed environment. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. Amazon S3. 
B. Amazon AppStream 2.0. 
C. AWS AppSync. 
D. AWS Outposts''',
     'respuesta': 'Amazon AppStream 2.0.',
     'argumento': 'As an application streaming / SaaS conversion service, AppStream 2.0 lets you move your desktop applications to AWS without rewriting them. It’s easy to install your applications on AppStream 2.0, set launch configurations, and make your applications available to users.',
     'referencia': 'https://aws.amazon.com/appstream2/faqs/?nc=sn&loc=7'},
    {'pregunta': 'A company wants to implement threat detection on its AWS infrastructure. However, the company does not want to deploy additional software. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. Amazon VPC. 
B. Amazon EC2. 
C. Amazon GuardDuty. 
D. AWS Direct Connect''',
     'respuesta': 'Amazon GuardDuty',
     'argumento': 'Amazon GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and delivers detailed security findings for visibility and remediation.',
     'referencia': 'https://aws.amazon.com/guardduty/'},
    {'pregunta': 'Which AWS service uses edge locations?',
     'opciones': '''A. Amazon Aurora. 
B. AWS Global Accelerator. 
C. Amazon Connect. 
D. AWS Outposts''',
     'respuesta': 'AWS Global Accelerator.',
     'argumento': 'AWS Global Accelerator and Amazon CloudFront are separate services that use the AWS global network and its edge locations around the world. CloudFront improves performance for both cacheable content (such as images and videos) and dynamic content (such as API acceleration and dynamic site delivery). Global Accelerator improves performance for a wide range of applications over TCP or UDP by proxying packets at the edge to applications running in one or more AWS Regions.',
     'referencia': 'https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works.html'},
    {'pregunta': 'A company needs to install an application in a Docker container. Which AWS service eliminates the need to provision and manage the container hosts?',
     'opciones': '''A. AWS Fargate. 
B. Amazon FSx for Windows File Server. 
C. Amazon Elastic Container Service (Amazon ECS). 
D. Amazon EC2''',
     'respuesta': 'Amazon Elastic Container Service (Amazon ECS)',
     'argumento': 'Amazon ECS eliminates the need for you to install and operate your own container orchestration software, manage and scale a cluster of virtual machines (VMs), or schedule containers on those VMs.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/containers.html#:~:text=Amazon%20ECS%20eliminates%20the%20need%20for%20you%20to%20install%20and%20operate%20your%20own%20container%20orchestration%20software%2C%20manage%20and%20scale%20a%20cluster%20of%20virtual%20machines%20(VMs)%2C%20or%20schedule%20containers%20on%20those%20VMs.'},
    {'pregunta': 'Which AWS service or feature checks access policies and offers actionable recommendations to help users set secure and functional policies?',
     'opciones': '''A. AWS Systems Manager. 
B. AWS IAM Access Analyzer. 
C. AWS Trusted Advisor. 
D. Amazon GuardDuty''',
     'respuesta': 'AWS IAM Access Analyzer',
     'argumento': 'Validate the policies you create to ensure that they adhere to the IAM policy language (JSON) and IAM best practices. You can validate your policies by using IAM Access Analyzer policy validation. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html'}, #70
    {'pregunta': 'A company has a fleet of cargo ships. The cargo ships have sensors that collect data at sea, where there is intermittent or no internet connectivity. The company needs to collect, format, and process the data at sea and move the data to AWS later. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS IoT Core. 
B. Amazon Lightsail. 
C. AWS Storage Gateway. 
D. AWS Snowball Edge''',
     'respuesta': 'AWS Storage Gateway',
     'argumento': 'AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage. it indicate that the ships have intermitent internet connection so the storage gw match for the purpose, the snowball will be if it has not internet connection.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/8/'},
    {'pregunta': 'A retail company needs to build a highly available architecture for a new ecommerce platform. The company is using only AWS services that replicate data across multiple Availability Zones. Which AWS services should the company use to meet this requirement? (Choose two.)',
     'opciones': '''A. Amazon EC2. 
B. Amazon Elastic Block Store (Amazon EBS). 
C. Amazon Aurora. 
D. Amazon DynamoDB. 
E. Amazon Redshift''',
     'respuesta': '''A. Amazon EC2. 
B. Amazon Elastic Block Store (Amazon EBS)''',
     'argumento': 'Amazon EBS volumes are designed to be highly available, reliable, and durable. At no additional charge to you, Amazon EBS volume data is replicated across multiple servers in an Availability Zone to prevent the loss of data from the failure of any single component.',
     'referencia': 'https://aws.amazon.com/ebs/faqs/?nc1=h_ls'},
    {'pregunta': 'Which characteristic of the AWS Cloud helps users eliminate underutilized CPU capacity?',
     'opciones': '''A. Agility. 
B. Elasticity. 
C. Reliability. 
D. Durability''',
     'respuesta': 'Elasticity.',
     'argumento': 'AWS provides an elastic infrastructure that allows users to easily scale their computing resources up or down as needed, without having to worry about the underlying infrastructure. With AWS, users can provision resources to match their current needs and scale automatically to meet their future demands. This allows users to eliminate underutilized CPU capacity and optimize their resources for cost and performance.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/8/'},
    {'pregunta': 'Service control policies (SCPs) manage permissions for which of the following?',
     'opciones': '''A. Availability Zones. 
B. AWS Regions. 
C. AWS Organizations. 
D. Edge locations''',
     'respuesta': 'AWS Organizations.',
     'argumento': 'An AWS Service Control Policy (SCP) is a set of rules you can create to control access to your AWS resources within the AWS accounts in your AWS Organization.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html'},
    {'pregunta': 'Which AWS service can be used to encrypt data at rest?',
     'opciones': '''A. Amazon GuardDuty. 
B. AWS Shield. 
C. AWS Security Hub. 
D. AWS Key Management Service (AWS KMS)''',
     'respuesta': 'AWS Key Management Service (AWS KMS)',
     'argumento': 'AWS Key Management Service (KMS) is a fully managed service that allows you to create and manage encryption keys to protect your data. It provides a secure and centralized location for generating and controlling the encryption keys used to encrypt and decrypt your data. With AWS KMS, you can encrypt your data at rest by using AWS managed keys or by creating and importing your own keys. You can integrate KMS with various AWS services, such as Amazon S3, Amazon EBS, Amazon RDS, and others, to enable automatic encryption of data at rest.',
     'referencia': 'https://aws.amazon.com/blogs/security/how-to-protect-data-at-rest-with-amazon-ec2-instance-store-encryption/'}, #75
    {'pregunta': 'Which characteristics are advantages of using the AWS Cloud? (Choose two.)',
     'opciones': '''A. A 100% service level agreement (SLA) for all AWS services. 
B. Compute capacity that is adjusted on demand. 
C. Availability of AWS Support for code development. 
D. Enhanced security. 
E. Increases in cost and complexity''',
     'respuesta': '''B. Compute capacity that is adjusted on demand. 
D. Enhanced security.''',
     'argumento': 'Compute capacity that is adjusted on demand: One of the key benefits of the AWS Cloud is its elasticity, allowing users to scale their compute resources up or down based on demand. This flexibility enables users to optimize resource allocation and only pay for the resources they actually need. Enhanced security: AWS provides a secure infrastructure and offers a wide range of security services and features to help users protect their data and applications. These include encryption options, identity and access management controls, network security, monitoring tools, and compliance certifications. AWS follows security best practices and offers a shared responsibility model, where both AWS and the customer have responsibilities for security.',
     'referencia': 'https://intellipaat.com/blog/aws-benefits-and-drawbacks/'},
    {'pregunta': 'A user is storing objects in Amazon S3. The user needs to restrict access to the objects to meet compliance obligations. What should the user do to meet this requirement?',
     'opciones': '''A. Use AWS Secrets Manager. 
B. Tag the objects in the S3 bucket. 
C. Use security groups. 
D. Use network ACLs.''',
     'respuesta': 'Use network ACLs.',
     'argumento': 'To restrict access to objects stored in Amazon S3, the user should use Access Control Lists (ACLs) or Bucket Policies. Access Control Lists (ACLs) enable you to manage access to individual objects in an S3 bucket.',
     'referencia': 'https://repost.aws/knowledge-center/secure-s3-resources'},
    {'pregunta': 'A company wants to convert video files and audio files from their source format into a format that will play on smartphones, tablets, and web browsers. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon Elastic Transcoder. 
B. Amazon Comprehend. 
C. AWS Glue. 
D. Amazon Rekognition''',
     'respuesta': 'Amazon Elastic Transcoder.',
     'argumento': 'Amazon Elastic Transcoder is media transcoding in the cloud. It is designed to be a highly scalable, easy to use and a cost effective way for developers and businesses to convert (or “transcode”) media files from their source format into versions that will playback on devices like smartphones, tablets and PCs.',
     'referencia': 'https://aws.amazon.com/elastictranscoder/#:~:text=Amazon%20Elastic%20Transcoder%20is,smartphones%2C%20tablets%20and%20PCs.'},
    {'pregunta': 'https://aws.amazon.com/elastictranscoder/#:~:text=Amazon%20Elastic%20Transcoder%20is,smartphones%2C%20tablets%20and%20PCs.',
     'opciones': '''A. Improved health and availability of applications. 
B. Reduced network latency. 
C. Optimized performance and costs. 
D. Automated snapshots of data. 
E. Cross-Region Replication''',
     'respuesta': '''A. Improved health and availability of applications. 
C. Optimized performance and costs.''',
     'argumento': 'Improved health and availability of applications: Amazon EC2 Auto Scaling helps ensure the health and availability of applications by automatically adjusting the number of EC2 instances based on demand. It scales the instances up or down based on predefined scaling policies, helping to maintain optimal performance and availability. Optimized performance and costs: With Amazon EC2 Auto Scaling, you can set scaling policies to dynamically adjust the number of EC2 instances based on metrics such as CPU utilization, network traffic, or other custom metrics. This allows you to optimize your application´s performance by scaling resources up during high-demand periods and scaling down during low-demand periods, helping to minimize costs.',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html'},
    {'pregunta': 'A company has several departments. Each department has its own AWS accounts for its applications. The company wants all AWS costs on a single invoice to simplify payment, but the company wants to know the costs that each department is incurring. Which AWS tool or feature will provide this functionality?',
     'opciones': '''A. AWS Cost and Usage Reports. 
B. Consolidated billing. 
C. Savings Plans. 
D. AWS Budgets''',
     'respuesta': 'Consolidated billing',
     'argumento': 'Consolidated billing enables the company to consolidate payment for multiple AWS accounts or multiple departments into a single payment, making it easier to track and pay AWS costs. However, each AWS account remains separate, and each department can view its own usage and cost data',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html'}, #80
    {'pregunta': 'A company runs its workloads on premises. The company wants to forecast the cost of running a large application on AWS. Which AWS service or tool can the company use to obtain this information?',
     'opciones': '''A. AWS Pricing Calculator. 
B. AWS Budgets. 
C. AWS Trusted Advisor. 
D. Cost Explorer''',
     'respuesta': 'Cost Explorer',
     'argumento': 'You create a forecast by selecting a future time range for your report. For more information, see Choosing time ranges for the data that you want to view. The following section discusses the accuracy of the forecasts created by Cost Explorer and how to read them.',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-forecast.html'},
    {'pregunta': 'A company wants to eliminate the need to guess infrastructure capacity before deployments. The company also wants to spend its budget on cloud resources only as the company uses the resources. Which advantage of the AWS Cloud matches the company´s requirements?',
     'opciones': '''A. Reliability. 
B. Global reach. 
C. Economies of scale. 
D. Pay-as-you-go pricing''',
     'respuesta': 'Pay-as-you-go pricing',
     'argumento': 'Pay-as-you-go pricing allows the company to only pay for the resources they use, without having to guess how much infrastructure capacity they will need in advance. This means that the company can use cloud resources as needed and can scale up or down depending on demand, without having to worry about overprovisioning or underprovisionin',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which AWS service supports a hybrid architecture that gives users the ability to extend AWS infrastructure, AWS services, APIs, and tools to data centers, co- location environments, or on-premises facilities?',
     'opciones': '''A. AWS Snowmobile. 
B. AWS Local Zones. 
C. AWS Outposts. 
D. AWS Fargate''',
     'respuesta': 'AWS Outposts.',
     'argumento': 'AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. Outposts solutions allow you to extend and run native AWS services on premises, and is available in a variety of form factors, from 1U and 2U Outposts servers to 42U Outposts racks, and multiple rack deployments.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/localzones/, https://aws.amazon.com/outposts/'},
    {'pregunta': 'A company has a physical tape library to store data backups. The tape library is running out of space. The company needs to extend the tape library´s capacity to the AWS Cloud. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. Amazon Elastic Block Store (Amazon EBS). 
B. Amazon S3. 
C. Amazon Elastic File System (Amazon EFS). 
D. AWS Storage Gateway''',
     'respuesta': 'AWS Storage Gateway',
     'argumento': 'AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage.',
     'referencia': 'https://aws.amazon.com/storagegateway/'},
    {'pregunta': 'An online retail company has seasonal sales spikes several times a year, primarily around holidays. Demand is lower at other times. The company finds it difficult to predict the increasing infrastructure demand for each season. Which advantages of moving to the AWS Cloud would MOST benefit the company? (Choose two.)',
     'opciones': '''A. Global footprint. Elasticity. 
B. AWS service quotas. 
C. AWS shared responsibility model. 
D. Pay-as-you-go pricing''',
     'respuesta': 'Elasticity. Pay-as-you-go pricing.',
     'argumento': 'Elasticity allows the company to scale its infrastructure up or down as demand fluctuates. This is important for a company that experiences seasonal sales spikes, as they can easily increase their capacity during busy periods and then decrease it when demand is lower. Pay-as-you-go pricing means that the company only pays for the resources they use. This is beneficial for a company that experiences unpredictable demand, as they only have to pay for the resources they actually need.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'}, #85
    {'pregunta': 'Which AWS service can be used to turn text into lifelike speech?',
     'opciones': '''A. Amazon Polly. 
B. Amazon Kendra. 
C. Amazon Rekognition. 
D. Amazon Connect''',
     'respuesta': 'Amazon Polly.',
     'argumento': 'Amazon Polly is a service that can be used to turn text into lifelike speech. Amazon Polly uses advanced deep learning technologies to synthesize speech that sounds natural and lifelike, allowing users to convert written content into spoken language.',
     'referencia': 'https://aws.amazon.com/polly/#:~:text=Amazon%20Polly%20is%20a%20service,synthesize%20natural%20sounding%20human%20speech'},
    {'pregunta': 'Which AWS service or tool can be used to capture information about inbound and outbound traffic in an Amazon VPC?',
     'opciones': '''A. VPC Flow Logs. 
B. Amazon Inspector. 
C. VPC endpoint services. 
D. NAT gateway''',
     'respuesta': 'VPC Flow Logs',
     'argumento': 'VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to the following locations: Amazon CloudWatch Logs, Amazon S3, or Amazon Kinesis Data Firehose. After you create a flow log, you can retrieve and view the flow log records in the log group, bucket, or delivery stream that you configured',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html'},
    {'pregunta': 'A company wants to ensure that two Amazon EC2 instances are in separate data centers with minimal communication latency between the data centers. How can the company meet this requirement?',
     'opciones': '''A. Place the EC2 instances in two separate AWS Regions connected with a VPC peering connection. 
B. Place the EC2 instances in two separate Availability Zones within the same AWS Region. 
C. Place one EC2 instance on premises and the other in an AWS Region. Then connect them by using an AWS VPN connection. 
D. Place both EC2 instances in a placement group for dedicated bandwidth.''',
     'respuesta': '''Place the EC2 instances in two separate Availability Zones within the same AWS Region.''',
     'argumento': 'in the same AvZone the latency will be lower. Actually the placement group will be a choice but it did not give the option to differenciate the datacenter between the EC2 instance.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html'},
    {'pregunta': 'In which situations should a company create an IAM user instead of an IAM role? (Choose two.)',
     'opciones': '''A. When an application that runs on Amazon EC2 instances requires access to other AWS services. 
B. When the company creates AWS access credentials for individuals. 
C. When the company creates an application that runs on a mobile phone that makes requests to AWS. 
D. When the company needs to add users to IAM groups. 
E. When users are authenticated in the corporate network and want to be able to use AWS without having to sign in a second time''',
     'respuesta': '''B. When the company creates AWS access credentials for individuals. 
D. When the company needs to add users to IAM groups.''',
     'argumento': 'IAM users are designed for individuals who need to access AWS resources. They have long-term credentials that can be used to sign in to the AWS Management Console or to make requests to AWS services programmatically. IAM users can be configured to use single sign-on (SSO) with an identity provider (IdP), such as Active Directory or Okta. This allows users to sign in to the corporate network once, and then they will be automatically authenticated to AWS without having to enter their credentials again.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html'},
    {'pregunta': 'Which AWS services should a company use to read and write data that changes frequently? (Choose two.)',
     'opciones': '''A. Amazon S3 Glacier. 
B. Amazon RDS. AWS Snowball. 
C. Amazon Redshift. 
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'Amazon RDS. Amazon Redshift.',
     'argumento': 'Amazon DynamoDB is a fully managed NoSQL database service that is designed for high scale and performance. DynamoDB allows you to store and retrieve data with very low latency, making it well-suited for applications that require fast access to data. Amazon Redshift is a fast, fully managed data warehouse service that allows you to efficiently analyze large amounts of data using SQL and your existing business intelligence tools. Redshift is designed to handle data that changes frequently and can be used to store and analyze data in near real-time.',
     'referencia': 'https://aws.amazon.com/solutions/case-studies/nasdaq-case-study/?pg=ln&sec=c'}, #90
    {'pregunta': 'Which AWS service is used to provide encryption for Amazon EBS?',
     'opciones': '''A. AWS Certificate Manager. 
B. AWS Systems Manager. 
C. AWS KMS. 
D. AWS Config''',
     'respuesta': 'AWS KMS',
     'argumento': 'AWS Key Management Service (KMS) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2, or are in the process of being validated, to protect your keys. AWS KMS is integrated with AWS CloudTrail to provide you with logs of all key usage to help meet your regulatory and compliance needs.',
     'referencia': 'https://aws.amazon.com/kms/?nc1=h_ls'},
    {'pregunta': 'Which AWS services make use of global edge locations? (Choose two.)',
     'opciones': '''A. AWS Fargate. 
B. Amazon CloudFront. 
C. AWS Global Accelerator. 
D. AWS Wavelength. 
E. Amazon VPC''',
     'respuesta': '''B. Amazon CloudFront. 
C. AWS Global Accelerator''',
     'argumento': 'Amazon CloudFront: Amazon CloudFront is a content delivery network (CDN) service that uses a global network of edge locations to deliver content to users with low latency and high transfer speeds. The edge locations cache content and serve it from the location closest to the end users, improving performance and reducing the load on the origin server. AWS Global Accelerator: AWS Global Accelerator is a networking service that utilizes the AWS global network infrastructure to improve the availability and performance of applications. It uses a network of global edge locations to route user traffic to the nearest edge location, reducing latency and improving the responsiveness of applications.',
     'referencia': 'https://aws.amazon.com/cloudfront/features/?p=ugi&l=na&whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc'},
    {'pregunta': 'A company is operating several factories where it builds products. The company needs the ability to process data, store data, and run applications with local system interdependencies that require low latency. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS IoT Greengrass. 
B. AWS Lambda. 
C. AWS Outposts. 
D. AWS Snowball Edge''',
     'respuesta': 'AWS Outposts.',
     'argumento': 'By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.',
     'referencia': 'https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html'},
    {'pregunta': 'Which of the following is a recommended design principle for AWS Cloud architecture?',
     'opciones': '''A. Design tightly coupled components. 
B. Build a single application component that can handle all the application functionality. 
C. Make large changes on fewer iterations to reduce chances of failure. 
D. Avoid monolithic architecture by segmenting workloads.''',
     'respuesta': 'Avoid monolithic architecture by segmenting workloads.',
     'argumento': 'The recommended design principle for AWS Cloud architecture is to avoid monolithic architecture by segmenting workloads. Therefore, the correct answer is D. By segmenting workloads, you can isolate different parts of your application and make them more modular, which can lead to greater flexibility, scalability, and fault tolerance. It also allows you to use different technologies and tools for different parts of the application, which can make it easier to optimize each part for its specific requirements.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_monolith_soa_microservice.html'},
    {'pregunta': 'Which of the following acts as an instance-level firewall to control inbound and outbound access?',
     'opciones': '''A. Network access control list. 
B. Security groups. 
C. AWS Trusted Advisor. 
D. Virtual private gateways''',
     'respuesta': 'Security groups.',
     'argumento': 'Security groups in AWS act as an instance-level firewall to control inbound and outbound access to Amazon EC2 instances. They operate at the instance level and are associated with a specific instance or group of instances. Security groups allow you to define rules that specify the allowed inbound and outbound traffic based on protocols, ports, and IP addresses. They provide a stateful firewall, meaning that they track the state of a connection and automatically allow the return traffic for established connections.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html'}, #95
    {'pregunta': 'A company is designing its AWS workloads so that components can be updated regularly and so that changes can be made in small, reversible increments. Which pillar of the AWS Well-Architected Framework does this design support?',
     'opciones': '''A. Security. 
B. Performance efficiency. 
C. Operational excellence. 
D. Reliability''',
     'respuesta': 'Operational excellence.',
     'argumento': 'There are five design principles for operational excellence in the cloud: Perform operations as code Make frequent, small, reversible changes Refine operations procedures frequently Anticipate failure Learn from all operational failures',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html'},
    {'pregunta': 'A company has a workload that will run continuously for 1 year. The workload cannot tolerate service interruptions. Which Amazon EC2 purchasing option will be MOST cost-effective?',
     'opciones': '''A. All Upfront Reserved Instances. 
B. Partial Upfront Reserved Instances. 
C. Dedicated Instances. 
D. On-Demand Instances''',
     'respuesta': 'All Upfront Reserved Instances.',
     'argumento': 'With the All Upfront option, you pay for the entire Reserved Instance term with one upfront payment. This option provides you with the largest discount compared to On-Demand Instance pricing.',
     'referencia': 'https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/'},
    {'pregunta': 'Which AWS service helps protect against DDoS attacks?',
     'opciones': '''A. AWS Shield. 
B. Amazon Inspector. 
C. Amazon GuardDuty. 
D. Amazon Detective''',
     'respuesta': 'AWS Shield.',
     'argumento': 'AWS Shield is an AWS service that helps protect against Distributed Denial of Service (DDoS) attacks. It provides protection for AWS resources such as Amazon EC2 instances, Elastic Load Balancers, and Amazon CloudFront distributions. AWS Shield offers both Standard and Advanced tiers.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/10/, Question #98'},
    {'pregunta': 'Using AWS Config to record, audit, and evaluate changes to AWS resources to enable traceability is an example of which AWS Well-Architected Framework pillar?',
     'opciones': '''A. Security. 
B. Operational excellence. 
C. Performance efficiency. 
D. Cost optimization''',
     'respuesta': 'Security.',
     'argumento': 'Enable traceability: Monitor, alert, and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action.',
     'referencia': 'https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf '},
    {'pregunta': 'Which AWS tool or feature acts as a VPC firewall at the subnet level?',
     'opciones': '''A. Security group. 
B. Network ACL. 
C. Traffic Mirroring. 
D. Internet gateway''',
     'respuesta': 'Network ACL.',
     'argumento': 'A Network ACL is a feature of Amazon Virtual Private Cloud (VPC) that acts as a firewall at the subnet level. It is an optional layer of security that controls inbound and outbound traffic at the subnet level. A Network ACL operates at the protocol and port level and uses numbered rules to allow or deny traffic. By default, a Network ACL allows all inbound and outbound traffic.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html'}, #100
    {'pregunta': 'Which AWS service can be used to decouple applications?',
     'opciones': '''A. AWS Config. 
B. Amazon Simple Queue Service (Amazon SQS). 
C. AWS Batch. 
D. Amazon Simple Email Service (Amazon SES)''',
     'respuesta': 'Amazon Simple Queue Service (Amazon SQS).',
     'argumento': 'Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS moves data between distributed application components and helps you decouple these components.',
     'referencia': 'https://docs.aws.amazon.com/sqs/?id=docs_gateway'},
    {'pregunta': 'Which disaster recovery option is the LEAST expensive?',
     'opciones': '''A. Warm standby. 
B. Multisite. 
C. Backup and restore. 
D. Pilot light''',
     'respuesta': 'Backup and restore.',
     'argumento': 'Among the provided options, backup and restore is generally the least expensive disaster recovery option. It involves periodically backing up data and applications to a separate location or storage, and in the event of a disaster, restoring the backups to resume operations. This approach typically requires fewer resources and infrastructure compared to other options.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html'},
    {'pregunta': 'Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?',
     'opciones': '''A. Amazon Elastic Block Store (Amazon EBS). 
B. Amazon EC2 instance store. 
C. Amazon Elastic File System (Amazon EFS). 
D. Amazon S3''',
     'respuesta': 'Amazon EC2 instance store',
     'argumento': 'When you stop or terminate an instance, every block of storage in the instance store is reset. Therefore, your data cannot be accessed through the instance store of another instance.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html'},
    {'pregunta': 'Which of the following is a characteristic of the AWS account root user?',
     'opciones': '''A. The root user is the only user that can be configured with multi-factor authentication (MFA). 
B. The root user is the only user that can access the AWS Management Console. 
C. The root user is the first sign-in identity that is available when an AWS account is created. 
D. The root user has a password that cannot be changed.''',
     'respuesta': 'The root user is the first sign-in identity that is available when an AWS account is created.',
     'argumento': 'When an AWS account is created, the root user is automatically created as the first sign-in identity for that account. The root user has full administrative access to all resources and services within the AWS account. However, it is considered a security best practice to not use the root user for everyday tasks and to create additional IAM (Identity and Access Management) users with appropriate permissions.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html'},
    {'pregunta': 'A company hosts an application on an Amazon EC2 instance. The EC2 instance needs to access several AWS resources, including Amazon S3 and Amazon DynamoDB. What is the MOST operationally efficient solution to delegate permissions?',
     'opciones': '''A. Create an IAM role with the required permissions. Attach the role to the EC2 instance. 
B. Create an IAM user and use its access key and secret access key in the application. 
C. Create an IAM user and use its access key and secret access key to create a CLI profile in the EC2 instance.
D. Create an IAM role with the required permissions. Attach the role to the administrative IAM user.''',
     'respuesta': 'Create an IAM role with the required permissions. Attach the role to the administrative IAM user.',
     'argumento': 'When an EC2 instance needs to access AWS resources such as Amazon S3 and Amazon DynamoDB, it is recommended to use IAM roles. IAM roles are a secure way to grant temporary access to AWS services without the need to manage long-term credentials like access keys and secret access keys. By creating an IAM role with the necessary permissions and attaching it to the EC2 instance, the EC2 instance can assume the role and access the required AWS resources. This approach eliminates the need for managing access keys within the EC2 instance and provides a more secure and scalable solution.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html'}, #105
    {'pregunta': 'Which of the following is a component of the AWS Global Infrastructure?',
     'opciones': '''A. Amazon Alexa. 
B. AWS Regions. 
C. Amazon Lightsail. 
D. AWS Organizations''',
     'respuesta': 'AWS Regions.',
     'argumento': 'AWS Regions are a component of the AWS Global Infrastructure. AWS Regions are geographic locations around the world where AWS resources and services are available. Each AWS Region is isolated and independent, consisting of multiple Availability Zones. The AWS Global Infrastructure is the collective term for the network of AWS Regions and Availability Zones spread across different geographic locations.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/'},
    {'pregunta': 'What is the purpose of having an internet gateway within a VPC?',
     'opciones': '''A. To create a VPN connection to the VPC. 
B. To allow communication between the VPC and the internet. 
C. To impose bandwidth constraints on internet traffic. 
D. To load balance traffic from the internet across Amazon EC2 instances''',
     'respuesta': 'To allow communication between the VPC and the internet',
     'argumento': 'An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html'},
    {'pregunta': 'Which AWS service allows users to download security and compliance reports about the AWS infrastructure on demand?',
     'opciones': '''A. Amazon GuardDuty. 
B. AWS Security Hub. 
C. AWS Artifact. 
D. AWS Shield''',
     'respuesta': 'AWS Artifact',
     'argumento': 'AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to security and compliance reports from AWS and ISVs who sell their products on AWS Marketplace.',
     'referencia': 'https://aws.amazon.com/artifact/'},
    {'pregunta': 'A pharmaceutical company operates its infrastructure in a single AWS Region. The company has thousands of VPCs in a various AWS accounts that it wants to interconnect. Which AWS service or feature should the company use to help simplify management and reduce operational costs?',
     'opciones': '''A. VPC endpoint.
B. AWS Direct Connect.
C. AWS Transit Gateway.
D. VPC peering''',
     'respuesta': 'VPC peering',
     'argumento': 'VPC peering is point-to-point connectivity, and it does not support transitive routing. For example, if you have a VPC peering connection between VPC A and VPC B and between VPC A and VPC C, an instance in VPC B cannot transit through VPC A to reach VPC C. To route packets between VPC B and VPC C, you are required to create a direct VPC peering connection. At scale, when you have 10’s-100’s of VPCs, interconnecting them with peering results in a mesh of 100’s-1000’s of peering connections, which are difficult to manage and scale. There is a maximum limit of 125 peering connections per VPC.',
     'referencia': 'https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf'},
    {'pregunta': 'A company is planning an infrastructure deployment to the AWS Cloud. Before the deployment, the company wants a cost estimate for running the infrastructure. Which AWS service or feature can provide this information?',
     'opciones': '''A. Cost Explorer. 
B. AWS Trusted Advisor. 
C. AWS Cost and Usage Report. 
D. AWS Pricing Calculator''',
     'respuesta': 'AWS Pricing Calculator',
     'argumento': 'AWS Pricing Calculator is the AWS service or feature that can provide a cost estimate for running infrastructure before deployment. The AWS Pricing Calculator allows users to estimate the costs of using various AWS services based on their anticipated usage. It provides a web-based interface where users can select the desired AWS services, configure the specifications and quantities of resources needed, and define usage patterns. By inputting the details of the infrastructure deployment, such as the types and sizes of EC2 instances, storage volumes, networking resources, and other AWS services, the AWS Pricing Calculator can generate an estimated monthly cost for running the infrastructure in the AWS Cloud. This cost estimate can help the company plan its budget, evaluate different deployment options, and make informed decisions about the infrastructure design.',
     'referencia': 'https://aws.amazon.com/it/premiumsupport/knowledge-center/estimating-aws-resource-costs/'}, #110
    {'pregunta': 'Which AWS service of tool helps to centrally manage billing and allow controlled access to resources across AWS accounts?',
     'opciones': '''A. AWS Identity and Access Management (IAM)
B. AWS Organizations
C. Cost Explorer
D. AWS Budgets''',
     'respuesta': 'B. AWS Organizations',
     'argumento': 'AWS Organizations is the AWS service that helps centrally manage billing and allows controlled access to resources across multiple AWS accounts. AWS Organizations provides a way to centrally manage and govern multiple AWS accounts within an organization. It enables you to create and manage groups of accounts, called organizational units (OUs), to align with your company´s structure. With AWS Organizations, you can apply policies across those accounts, control access to resources, and consolidate billing.',
     'referencia': 'https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html'},
    {'pregunta': 'Which of the following are Amazon Virtual Private Cloud (Amazon VPC) resources?',
     'opciones': '''A. Objects; access control lists (ACLs)
B. Subnets; internet gateways
C. Access policies; buckets
D. Groups; roles''',
     'respuesta': 'B. Subnets; internet gateways',
     'argumento': 'Subnets are one of the key resources in Amazon VPC. They are subdivisions of IP address ranges within a VPC and provide a way to segment and isolate resources within your virtual network. Internet gateways are another important resource in Amazon VPC. They serve as the entry and exit points for traffic between your VPC and the internet. They enable communication between your VPC resources and external networks, such as the public internet.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html'},
    {'pregunta': 'A company needs to identify the last time that a specific user accessed the AWS Management Console. Which AWS service will provide this information?',
     'opciones': '''A. Amazon Cognito
B. AWS CloudTrail
C. Amazon Inspector
D. Amazon GuardDuty''',
     'respuesta': 'B. AWS CloudTrail',
     'argumento': 'AWS CloudTrail is a service that enables you to monitor and log user activity and API usage within your AWS account. It records actions taken by users, including console sign-in events, API calls, and management events, and stores them in a log file. This log file can be analyzed to gain visibility into user activity and track actions taken in the AWS Management Console. By examining the CloudTrail logs, you can identify the last time a specific user accessed the AWS Management Console. The logs will provide information about console sign-in events, including the user, timestamp, and source IP address.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/12/'},
    {'pregunta': 'A company launched an Amazon EC2 instance with the latest Amazon Linux 2 Amazon Machine Image (AMI). Which actions can a system administrator take to connect to the EC2 instance? (Choose two.)',
     'opciones': '''A. Use Amazon EC2 Instance Connect.
B. Use a Remote Desktop Protocol (RDP) connection.
C. Use AWS Batch
D. Use AWS Systems Manager Session Manager.
E. Use Amazon Connect''',
     'respuesta': '''A. Use Amazon EC2 Instance Connect.
D. Use AWS Systems Manager Session Manager.''',
     'argumento': 'Amazon EC2 Instance Connect is a secure and easy-to-use method for SSH access to EC2 instances. It allows system administrators to connect to their instances using the AWS Management Console or the AWS CLI without the need for managing SSH key pairs manually. AWS Systems Manager Session Manager provides interactive shell access to EC2 instances directly from the AWS Management Console or the AWS CLI. It does not require opening inbound SSH ports or managing SSH keys.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html'},
    {'pregunta': 'A company wants to perform sentiment analysis on customer service email messages that it receives. The company wants to identify whether the customer service engagement was positive or negative. Which AWS service should the company use to perform this analysis?',
     'opciones': '''A. Amazon Textract
B. Amazon Translate
C. Amazon Comprehend
D. Amazon Rekognition''',
     'respuesta': 'C. Amazon Comprehend',
     'argumento': 'Amazon Comprehend is a natural language processing (NLP) service offered by AWS. It provides pre-trained models to analyze text and extract insights, including sentiment analysis. With Amazon Comprehend, the company can easily determine the sentiment of customer service email messages, whether they are positive, negative, or neutral. This can help in understanding customer feedback and improving customer service strategies.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/12/'}, #115
    {'pregunta': 'What is the total amount of storage offered by Amazon S3?',
     'opciones': '''A. 100MB
B. 5 GB
C. 5 TB
D. Unlimited''',
     'respuesta': 'D. Unlimited',
     'argumento': 'The total volume of data and number of objects you can store are unlimited. Individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 TB.',
     'referencia': 'https://aws.amazon.com/s3/faqs/#:~:text=The%20total%20volume%20of%20data,a%20maximum%20of%205%20TB.'},
    {'pregunta': 'A company is migrating to Amazon S3. The company needs to transfer 60 TB of data from an on-premises data center to AWS within 10 days. Which AWS service should the company use to accomplish this migration?',
     'opciones': '''A. Amazon S3 Glacier
B. AWS Database Migration Service (AWS DMS)
C. AWS Snowball
D. AWS Direct Connect''',
     'respuesta': 'C. AWS Snowball',
     'argumento': 'AWS Snowball is a service specifically designed for large-scale data transfers. It allows you to securely and quickly transfer large amounts of data to and from AWS. In this scenario, where the company needs to transfer 60 TB of data within a limited timeframe, AWS Snowball would be the most suitable choice. The company can request a Snowball appliance from AWS, which will be shipped to their location. They can then load their data onto the Snowball appliance, ship it back to AWS, and AWS will transfer the data into an S3 bucket. This method ensures fast and efficient data transfer, even with large amounts of data.',
     'referencia': 'https://aws.amazon.com/snow/'},
    {'pregunta': 'What type of database is Amazon DynamoDB?',
     'opciones': '''A. In-memory
B. Relational
C. Key-value
D. Graph''',
     'respuesta': 'C. Key-value',
     'argumento': 'Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.',
     'referencia': 'https://aws.amazon.com/dynamodb/'},
    {'pregunta': 'A large organization has a single AWS account. What are the advantages of reconfiguring the single account into multiple AWS accounts? (Choose two.)',
     'opciones': '''A. It allows for administrative isolation between different workloads.
B. Discounts can be applied on a quarterly basis by submitting cases in the AWS Management Console.
C. Transitioning objects from Amazon S3 to Amazon S3 Glacier in separate AWS accounts will be less expensive.
D. Having multiple accounts reduces the risks associated with malicious activity targeted at a single account.
E. Amazon QuickSight offers access to a cost tool that provides application-specific recommendations for environments running in multiple accounts.''',
     'respuesta': '''A. It allows for administrative isolation between different workloads.
D. Having multiple accounts reduces the risks associated with malicious activity targeted at a single account.''',
     'argumento': '''A. It allows for administrative isolation between different workloads: By using multiple accounts, organizations can separate their workloads and resources, providing isolation and control over each workload. This helps in managing access, security, and resource allocation independently for different teams or projects.
D. Having multiple accounts reduces the risks associated with malicious activity targeted at a single account: If a single AWS account is compromised, all the resources and workloads within that account may be at risk. By using multiple accounts, the impact of a security breach or malicious activity can be limited to a specific account, reducing the overall risk.''',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html'},
    {'pregunta': 'A retail company has recently migrated its website to AWS. The company wants to ensure that it is protected from SQL injection attacks. The website uses an Application Load Balancer to distribute traffic to multiple Amazon EC2 instances. Which AWS service or feature can be used to create a custom rule that blocks SQL injection attacks?',
     'opciones': '''A. Security groups
B. AWS WAF
C. Network ACLs
D. AWS Shield''',
     'respuesta': 'B. AWS WAF',
     'argumento': 'AWS WAF is a web application firewall that helps protect web applications from common web exploits and vulnerabilities, including SQL injection attacks. With AWS WAF, you can create custom rules that inspect incoming requests and block any requests that match specific patterns or signatures associated with SQL injection attacks. By configuring AWS WAF with custom rules, you can define conditions and actions to be taken when SQL injection attempts are detected. These rules can be applied at the Application Load Balancer level, allowing you to protect your web application across multiple Amazon EC2 instances behind the load balancer.',
     'referencia': 'https://aws.amazon.com/waf/'}, #120
    {'pregunta': 'Which AWS service provides a feature that can be used to proactively monitor and plan for the service quotas of AWS resources?',
     'opciones': '''A. AWS CloudTrail
B. AWS Personal Health Dashboard
C. AWS Trusted Advisor
D. Amazon CloudWatch''',
     'respuesta': 'D. Amazon CloudWatch',
     'argumento': 'Monitor and proactively manage your service quotas You can see your quota utilization in the Service Quotas console. You can also create Amazon CloudWatch alarms for supported services. For more information, see Service Quotas and Amazon CloudWatch Alarms.',
     'referencia': 'https://aws.amazon.com/premiumsupport/knowledge-center/manage-service-limits/'},
    {'pregunta': 'Which of the following is an advantage that users experience when they move on-premises workloads to the AWS Cloud?',
     'opciones': '''A. Elimination of expenses for running and maintaining data centers
B. Price discounts that are identical to discounts from hardware providers
C. Distribution of all operational controls to AWS
D. Elimination of operational expenses''',
     'respuesta': 'A. Elimination of expenses for running and maintaining data centers',
     'argumento': 'Stop spending money running and maintaining data centers – Focus on projects that differentiate your business, not the infrastructure. Cloud computing lets you focus on your own customers, rather than on the heavy lifting of racking, stacking, and powering servers.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which design principle is included in the operational excellence pillar of the AWS Well-Architected Framework?',
     'opciones': '''A. Create annotated documentation.
B. Anticipate failure.
C. Ensure performance efficiency.
D. Optimize costs.''',
     'respuesta': 'B. Anticipate failure.',
     'argumento': 'Anticipate failure: Perform "pre-mortem" exercises to identify potential sources of failure so that they can be removed or mitigated. Test your failure scenarios and validate your understanding of their impact. Test your response procedures to ensure they are effective and that teams are familiar with their process. Set up regular game days to test workload and team responses to simulated events.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-excellence.html'},
    {'pregunta': 'Which AWS services offer gateway VPC endpoints that can be used to avoid sending traffic over the internet? (Choose two.)',
     'opciones': '''A. Amazon Simple Notification Service (Amazon SNS)
B. Amazon Simple Queue Service (Amazon SQS)
C. AWS CodeBuild
D. Amazon S3
E. Amazon DynamoDB''',
     'respuesta': '''D. Amazon S3
E. Amazon DynamoDB''',
     'argumento': 'Gateway VPC endpoints provide reliable connectivity to Amazon S3 and DynamoDB without requiring an internet gateway or a NAT device for your VPC. Gateway endpoints do not use AWS PrivateLink, unlike other types of VPC endpoints.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html'},
    {'pregunta': 'Which of the following is the customer responsible for updating and patching, according to the AWS shared responsibility model?',
     'opciones': '''A. Amazon FSx for Windows File Server
B. Amazon WorkSpaces virtual Windows desktop
C. AWS Directory Service for Microsoft Active Directory
D. Amazon RDS for Microsoft SQL Server''',
     'respuesta': 'B. Amazon WorkSpaces virtual Windows desktop',
     'argumento': 'We recommend that you regularly patch, update, and secure the operating system and applications on your WorkSpaces. You can configure your WorkSpaces to be updated by WorkSpaces during a regular maintenance window or you can update them yourself.',
     'referencia': 'https://docs.aws.amazon.com/workspaces/latest/adminguide/update-management.html'}, #125
    {'pregunta': 'Who has the responsibility to patch the host operating system of an Amazon EC2 instance, according to the AWS shared responsibility model?',
     'opciones': '''A. Both AWS and the customer
B. The customer only
C. The EC2 hardware manufacturer
D. AWS only''',
     'respuesta': '',
     'argumento': 'According to the AWS shared responsibility model, the responsibility to patch the host operating system of an Amazon EC2 instance falls on the customer, which means the correct answer is B. AWS is responsible for the security of the cloud infrastructure, including the physical security of the data centers, the security of the hypervisor, and the security of the networking and storage infrastructure. The customer is responsible for the security of their own applications and data, including the security of the guest operating system and any applications running on it. Therefore, the customer must ensure that the operating system of their EC2 instances is patched and up to date with the latest security patches and updates. AWS provides tools and services to help customers manage their EC2 instances, including the ability to automate patch management, but it is ultimately the responsibility of the customer to ensure that their instances are secure.',
     'referencia': 'https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg'},
    {'pregunta': 'A company is using an Amazon RDS DB instance for an application that is deployed in the AWS Cloud. The company needs regular patching of the operating system of the server where the DB instance runs. What is the company´s responsibility in this situation, according to the AWS shared responsibility model?',
     'opciones': '''A. Open a support case to obtain administrative access to the server so that the company can patch the DB instance operating system.
B. Open a support case and request that AWS patch the DB instance operating system.
C. Use administrative access to the server, and apply the operating system patches during the regular maintenance window that is defined for the DB instance.
D. Establish a regular maintenance window that tells AWS when to patch the DB instance operating system.''',
     'respuesta': 'B. Open a support case and request that AWS patch the DB instance operating system.',
     'argumento': 'Open a support case and request that AWS patch the DB instance operating system. According to the AWS shared responsibility model, the responsibility for patching the operating system of an Amazon RDS DB instance lies with AWS, not the customer. Therefore, in this situation, the company should open a support case and request that AWS patch the DB instance operating system.  Customers are responsible for ensuring that they apply any necessary updates and patches to their applications and data, but AWS is responsible for patching the underlying infrastructure, including the host operating system for Amazon RDS instances.',
     'referencia': 'https://go.aws/3EzIUmS'},
    {'pregunta': 'Why is an AWS Well-Architected review a critical part of the cloud design process?',
     'opciones': '''A. A Well-Architected review is mandatory before a workload can run on AWS.
B. A Well-Architected review helps identify design gaps and helps evaluate design decisions and related documents.
C. A Well-Architected review is an audit mechanism that is a part of requirements for service level agreements.
D. A Well-Architected review eliminates the need for ongoing auditing and compliance tests.''',
     'respuesta': 'B. A Well-Architected review helps identify design gaps and helps evaluate design decisions and related documents.',
     'argumento': 'An AWS Well-Architected review is a voluntary process that allows customers to assess their workloads against AWS architectural best practices. It helps identify areas where improvements can be made to optimize the workload for factors such as security, reliability, performance efficiency, cost optimization, and operational excellence. By conducting a Well-Architected review, organizations can gain insights into potential design gaps, identify areas for improvement, and ensure that their architecture aligns with AWS best practices. This review process helps validate the architecture´s adherence to AWS guidelines and provides recommendations for optimization, risk mitigation, and cost savings. The review is not mandatory for workloads to run on AWS, nor does it replace ongoing auditing and compliance requirements. Instead, it serves as a valuable tool in the cloud design process, assisting organizations in creating robust, well-architected solutions on AWS.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/the-review-process.html'},
    {'pregunta': 'A company implements an Amazon EC2 Auto Scaling policy along with an Application Load Balancer to automatically recover unhealthy applications that run on Amazon EC2 instances. Which pillar of the AWS Well-Architected Framework does this action cover?',
     'opciones': '''A. Security
B. Performance efficiency
C. Operational excellence
D. Reliability''',
     'respuesta': 'D. Reliability',
     'argumento': 'This provides for automatic notification and tracking of failures, and for automated recovery processes that work around or repair the failure. With more sophisticated automation, it’s possible to anticipate and remediate failures before they occur.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html'},
    {'pregunta': 'Which AWS Cloud benefit is shown by an architecture´s ability to withstand failures with minimal downtime?',
     'opciones': '''A. Agility
B. Elasticity
C. Scalability
D. High availability''',
     'respuesta': 'D. High availability',
     'argumento': 'By building a highly available architecture, organizations can minimize or eliminate the impact of failures on their applications and services. This is achieved through strategies such as redundancy, fault tolerance, and automatic failover. When failures occur, the architecture is designed to quickly and seamlessly recover and continue providing services to users, thereby minimizing or avoiding any downtime.',
     'referencia': 'https://aws.amazon.com/marketplace/solutions/infrastructure-software/high-availability'}, #130
    {'pregunta': 'Under the AWS shared responsibility model, which task is the customer´s responsibility when managing AWS Lambda functions?',
     'opciones': '''A. Creating versions of Lambda functions
B. Maintaining server and operating systems
C. Scaling Lambda resources according to demand
D. Updating the Lambda runtime environment''',
     'respuesta': 'A. Creating versions of Lambda functions',
     'argumento': 'By creating versions or aliases, the customer can have control over the different iterations of their Lambda functions and manage the deployment and testing of new code versions without impacting the production environment. This allows for better control and management of the function´s lifecycle.',
     'referencia': 'https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html'},
    {'pregunta': 'What does the AWS Concierge Support team provide?',
     'opciones': '''A. A technical expert dedicated to the user
B. A primary point of contact for AWS Billing and AWS Support
C. A partner to help provide scaling guidance for an event launch
D. A dedicated AWS staff member who reviews the user's application architecture''',
     'respuesta': 'B. A primary point of contact for AWS Billing and AWS Support',
     'argumento': 'Your Amazon Web Services Concierge is a senior customer service agent who is assigned to your account when you subscribe to an Enterprise or qualified Reseller Support plan. This Concierge agent is your primary point of contact for billing or account inquiries; when you don’t know whom to call, they will find the right people to help. In most cases, the Amazon Web Services Concierge is available during regular business hours in your headquarters’ geography. The best way to contact the Amazon Web Services Concierge is through the Amazon Web Services Support Center.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/enterprise/'},
    {'pregunta': 'A company needs to generate reports that can break down cloud costs by product, by company-defined tags, and by hour, day, and month. Which AWS tool should the company use to meet these requirements?',
     'opciones': '''A. Reserved Instance utilization and coverage reports
B. Savings Plans utilization reports
C. AWS Budgets reports
D. AWS Cost and Usage Reports''',
     'respuesta': 'D. AWS Cost and Usage Reports',
     'argumento': 'The AWS Cost and Usage Reports (AWS CUR) contains the most comprehensive set of cost and usage data available. You can use Cost and Usage Reports to publish your AWS billing reports to an Amazon Simple Storage Service (Amazon S3) bucket that you own. You can receive reports that break down your costs by the hour, day, or month, by product or product resource, or by tags that you define yourself. AWS updates the report in your bucket once a day in comma-separated value (CSV) format. You can view the reports using spreadsheet software such as Microsoft Excel or Apache OpenOffice Calc, or access them from an application using the Amazon S3 API.',
     'referencia': 'https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html'},
    {'pregunta': 'A company has a serverless application that includes an Amazon API Gateway API, an AWS Lambda function, and an Amazon DynamoDB database. Which AWS service can the company use to trace user requests as they move through the application´s components?',
     'opciones': '''A. AWS CloudTrail
B. Amazon CloudWatch
C. Amazon Inspector
D. AWS X-Ray''',
     'respuesta': 'D. AWS X-Ray',
     'argumento': 'AWS X-Ray provides a complete view of requests as they travel through your application and filters visual data across payloads, functions, traces, services, APIs, and more with no-code and low-code motions.',
     'referencia': 'https://aws.amazon.com/xray/'},
    {'pregunta': 'A company needs to set up a petabyte-scale data warehouse in the AWS Cloud. Which AWS service will meet this requirement?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Redshift
D. Amazon ElastiCache''',
     'respuesta': 'C. Amazon Redshift',
     'argumento': 'Amazon Redshift is a fully managed data warehousing service in the AWS Cloud. It is specifically designed to handle large-scale data analytics workloads, including petabyte-scale data warehouses. With Redshift, the company can store and analyze vast amounts of data efficiently and cost-effectively. It provides fast query performance, scalability, and easy integration with other AWS services and tools for data analytics and business intelligence.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/14/'}, #135
    {'pregunta': 'Which AWS service is always provided at no charge?',
     'opciones': '''A. Amazon S3
B. AWS Identity and Access Management (IAM)
C. Elastic Load Balancers
D. AWS WAF''',
     'respuesta': 'B. AWS Identity and Access Management (IAM)',
     'argumento': 'You can interact with IAM through the web-based IAM console, the AWS Command Line Interface, or the AWS API or SDKs. IAM is offered at no additional charge.',
     'referencia': 'https://aws.amazon.com/premiumsupport/knowledge-center/iam-intro/#:~:text=You%20can%20interact%20with%20IAM,offered%20at%20no%20additional%20charge.'},
    {'pregunta': 'A company needs to design an AWS disaster recovery plan to cover multiple geographic areas. Which action will meet this requirement?',
     'opciones': '''A. Configure multiple AWS accounts.
B. Configure the architecture across multiple Availability Zones in an AWS Region.
C. Configure the architecture across multiple AWS Regions.
D. Configure the architecture among many edge locations.''',
     'respuesta': 'C. Configure the architecture across multiple AWS Regions.',
     'argumento': 'In addition to data, you must also back up the configuration and infrastructure necessary to redeploy your workload and meet your Recovery Time Objective (RTO). AWS CloudFormation provides Infrastructure as Code (IaC), and enables you to define all of the AWS resources in your workload so you can reliably deploy and redeploy to multiple AWS accounts and AWS Regions. ',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html'},
    {'pregunta': 'Which of the following is a benefit of moving from an on-premises data center to the AWS Cloud?',
     'opciones': '''A. Compute instances can be launched and terminated as needed to optimize costs.
B. Compute costs can be viewed in the AWS Billing and Cost Management console.
C. Users retain full administrative access to their compute instances.
D. Users can optimize costs by permanently running enough instances at peak load.''',
     'respuesta': 'A. Compute instances can be launched and terminated as needed to optimize costs.',
     'argumento': 'One of the benefits of moving from an on-premises data center to the AWS Cloud is the ability to leverage the elasticity and scalability of cloud computing. With AWS, users can launch and terminate compute instances (such as Amazon EC2 instances) as needed based on the demand and workload requirements. This allows for optimized cost management, as users only pay for the resources they actually use and can scale up or down to match the workload. This flexibility in resource provisioning is a key advantage of the AWS Cloud.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/14/'},
    {'pregunta': 'In which ways does the AWS Cloud offer lower total cost of ownership (TCO) of computing resources than on-premises data centers? (Choose two.)',
     'opciones': '''A. AWS replaces upfront capital expenditures with pay-as-you-go costs.
B. AWS is designed for high availability, which eliminates user downtime.
C. AWS eliminates the need for on-premises IT staff.
D. AWS uses economies of scale to continually reduce prices.
E. AWS offers a single pricing model for Amazon EC2 instances.''',
     'respuesta': '''A. AWS replaces upfront capital expenditures with pay-as-you-go costs.
D. AWS uses economies of scale to continually reduce prices.''',
     'argumento': 'A. AWS replaces upfront capital expenditures with pay-as-you-go costs: With AWS, users only pay for what they use, without the need for upfront investments in hardware, facilities, and maintenance. This pay-as-you-go model can result in significant cost savings, especially for organizations that have unpredictable or variable workloads. D. AWS uses economies of scale to continually reduce prices: AWS operates at a large scale, and as a result, they can offer computing resources at lower prices than on-premises data centers. Additionally, AWS regularly reduces prices for its services as it gains more customers and achieves greater economies of scale.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which AWS service monitors AWS accounts for security threats?',
     'opciones': '''A. Amazon GuardDuty
B. AWS Secrets Manager
C. Amazon Cognito
D. AWS Certificate Manager (ACM)''',
     'respuesta': 'A. Amazon GuardDuty',
     'argumento': 'Amazon GuardDuty is the AWS service that monitors AWS accounts for security threats. It continuously analyzes logs and network traffic data to detect malicious activity, unauthorized behavior, and potential security risks. GuardDuty uses machine learning and threat intelligence to identify threats such as account compromise, data exfiltration, and suspicious API activity. When it detects a security issue, it generates findings and sends alerts to help users take appropriate actions to remediate the threat.',
     'referencia': 'https://aws.amazon.com/guardduty/'}, #140
    {'pregunta': 'Which benefit is included with an AWS Enterprise Support plan?',
     'opciones': '''A. AWS Partner Network (APN) support at no cost.
B. Designated support from an AWS technical account manager (TAM)
C. On-site support from AWS engineers
D. AWS managed compliance as code with AWS Config''',
     'respuesta': 'B. Designated support from an AWS technical account manager (TAM)',
     'argumento': "\With an AWS Enterprise Support plan, one of the benefits is the availability of a designated AWS technical account manager (TAM). The TAM acts as a single point of contact and provides personalized guidance and assistance to help the customer optimize their AWS environment, resolve technical issues, and achieve their business goals. The TAM works closely with the customer to understand their specific needs and provides proactive support, architectural guidance, and best practices recommendations.",
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/15/'},
    {'pregunta': 'Which task does AWS perform automatically?',
     'opciones': '''A. Encrypt data that is stored in Amazon DynamoDB.
B. Patch Amazon EC2 instances.
C. Encrypt user network traffic.
D. Create TLS certificates for users' websites.''',
     'respuesta': 'A. Encrypt data that is stored in Amazon DynamoDB.',
     'argumento': 'All user data stored in Amazon DynamoDB is fully encrypted at rest. DynamoDB encryption at rest provides enhanced security by encrypting all your data at rest using encryption keys stored in AWS Key Management Service (AWS KMS). This functionality helps reduce the operational burden and complexity involved in protecting sensitive data. With encryption at rest, you can build security-sensitive applications that meet strict encryption compliance and regulatory requirements.',
     'referencia': 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html'},
    {'pregunta': 'Which AWS service or tool can a company use to visualize, understand, and manage AWS spending and usage over time?',
     'opciones': '''A. AWS Trusted Advisor
B. Amazon CloudWatch
C. Cost Explorer
D. AWS Budgets''',
     'respuesta': 'C. Cost Explorer',
     'argumento': 'AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. Get started quickly by creating custom reports that analyze cost and usage data. Analyze your data at a high level (for example, total costs and usage across all accounts), or dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'},
    {'pregunta': 'A company wants to deploy some of its resources in the AWS Cloud. To meet regulatory requirements, the data must remain local and on premises. There must be low latency between AWS and the company resources. Which AWS service or feature can be used to meet these requirements?',
     'opciones': '''A. AWS Local Zones
B. Availability Zones
C. AWS Outposts
D. AWS Wavelength Zones''',
     'respuesta': 'A. AWS Local Zones',
     'argumento': 'Question says "deploy applications". Use case of AWS Local Zone : Run low-latency applications at the edge Build and deploy applications close to end users to enable real-time gaming, live streaming, augmented and virtual reality (AR/VR), virtual workstations, and more. Simplify hybrid cloud migrations Migrate your applications to a nearby AWS Local Zone, while still meeting the low-latency requirements of hybrid deployment.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/localzones/'},
    {'pregunta': 'A company requires an isolated environment within AWS for security purposes. Which action can be taken to accomplish this?',
     'opciones': '''A. Create a separate Availability Zone to host the resources.
B. Create a separate VPC to host the resources.
C. Create a placement group to host the resources.
D. Create an AWS Direct Connect connection between the company and AWS.''',
     'respuesta': 'B. Create a separate VPC to host the resources.',
     'argumento': 'To create an isolated environment within AWS for security purposes, the company can create a separate Virtual Private Cloud (VPC). A VPC is a logically isolated section of the AWS Cloud where the company can launch AWS resources in a virtual network that is dedicated to their account. By creating a separate VPC, the company can control the network settings, IP address ranges, subnets, route tables, and security settings specific to their isolated environment.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/infrastructure-security.html'}, #145
    {'pregunta': 'Which AWS service is a highly available and scalable DNS web service?',
     'opciones': '''A. Amazon VPC
B. Amazon CloudFront
C. Amazon Route 53
D. Amazon Connect''',
     'respuesta': 'C. Amazon Route 53',
     'argumento': 'Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service provided by AWS. It is designed to route end users to internet applications by translating domain names into IP addresses. Route 53 provides reliable and cost-effective domain registration, DNS routing, and health checking of resources within AWS or outside of it.',
     'referencia': 'https://aws.amazon.com/route53/'},
    {'pregunta': 'Which of the following is an AWS best practice for managing an AWS account root user?',
     'opciones': '''A. Keep the root user password with the security team.
B. Enable multi-factor authentication (MFA) for the root user.
C. Create an access key for the root user.
D. Keep the root user password consistent for compliance purposes.''',
     'respuesta': 'B. Enable multi-factor authentication (MFA) for the root user.',
     'argumento': 'Safeguard your root user credentials by configuring MFA for your root user credentials. We don´t recommend generating access keys for your root user, because they allow full access to all your resources.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html'},
    {'pregunta': 'A company wants to improve its security and audit posture by limiting Amazon EC2 inbound access. What should the company use to access instances remotely instead of opening inbound SSH ports and managing SSH keys?',
     'opciones': '''A. EC2 key pairs
B. AWS Systems Manager Session Manager
C. AWS Identity and Access Management (IAM)
D. Network ACLs''',
     'respuesta': 'B. AWS Systems Manager Session Manager',
     'argumento': 'AWS Systems Manager Session Manager is a new interactive shell and CLI that helps to provide secure, access-controlled, and audited Windows and Linux EC2 instance management. Session Manager removes the need to open inbound ports, manage SSH keys, or use bastion hosts.',
     'referencia': 'https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html'},
    {'pregunta': 'After selecting an Amazon EC2 Dedicated Host reservation, which pricing option would provide the largest discount?',
     'opciones': '''A. No upfront payment
B. Hourly on-demand payment
C. Partial upfront payment
D. All upfront payment''',
     'respuesta': 'D. All upfront payment',
     'argumento': 'you can choose between three payment options when you purchase a Standard or Convertible Reserved Instance. With the All Upfront option, you pay for the entire Reserved Instance term with one upfront payment. This option provides you with the largest discount compared to On-Demand Instance pricing',
     'referencia': 'https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/'},
    {'pregunta': 'A company has refined its workload to use specific AWS services to improve efficiency and reduce cost. Which best practice for cost governance does this example show?',
     'opciones': '''A. Resource controls
B. Cost allocation
C. Architecture optimization
D. Tagging enforcement''',
     'respuesta': 'B. Cost allocation',
     'argumento': 'These services remove the need for you to manage a resource, and provide the function of code execution, queuing services, and message delivery. The other benefit is that they scale in performance and cost in line with usage, allowing efficient cost allocation and attribution.',
     'referencia': 'https://d1.awsstatic.com/whitepapers/architecture/AWS-Cost-Optimization-Pillar.pdf'}, #150
    {'pregunta': 'A company would like to host its MySQL databases on AWS and maintain full control over the operating system, database installation, and configuration. Which AWS service should the company use to host the databases?',
     'opciones': '''A. Amazon RDS
B. Amazon EC2
C. Amazon DynamoDB
D. Amazon Aurora''',
     'respuesta': 'B. Amazon EC2',
     'argumento': '-Hosting a MySQL database on an EC2 instance, you will be able to choose the underlying building blocks such as operating system, storage settings, and database configuration, giving you full control and flexibility over your MySQL database and surpassing the limitations of Amazon RDS, while also leveraging all the advantages of the AWS Cloud platform and services.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html'},
    {'pregunta': 'How does the AWS global infrastructure offer high availability and fault tolerance to its users?',
     'opciones': '''A. The AWS infrastructure is made up of multiple AWS Regions within various Availability Zones located in areas that have low flood risk, and are interconnected with low-latency networks and redundant power supplies.
B. The AWS infrastructure consists of subnets containing various Availability Zones with multiple data centers located in the same geographic location.
C. AWS allows users to choose AWS Regions and data centers so that users can select the closest data centers in different Regions.
D. The AWS infrastructure consists of isolated AWS Regions with independent Availability Zones that are connected with low-latency networking and redundant power supplies.''',
     'respuesta': 'D. The AWS infrastructure consists of isolated AWS Regions with independent Availability Zones that are connected with low-latency networking and redundant power supplies',
     'argumento': 'AWS achieves high availability and fault tolerance for its users by building its infrastructure on top of independent AWS Regions, which are made up of separate Availability Zones. Each Availability Zone is physically isolated and located in a separate geographic location with redundant power, networking, and connectivity to other zones within the same region. This isolation and redundancy ensure that even if one Availability Zone fails, other zones within the same region continue to operate normally',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/16/'},
    {'pregunta': 'A company is using Amazon EC2 Auto Scaling to scale its Amazon EC2 instances. Which benefit of the AWS Cloud does this example illustrate?',
     'opciones': '''A. High availability
B. Elasticity
C. Reliability
D. Global reach''',
     'respuesta': 'A. High availability',
     'argumento': 'Amazon EC2 Auto Scaling will automatically replace unhealthy or unreachable instances to maintain higher availability of your applications.',
     'referencia': 'https://aws.amazon.com/ec2/autoscaling/features/'},
    {'pregunta': 'Which AWS service or feature is used to send both text and email messages from distributed applications?',
     'opciones': '''A. Amazon Simple Notification Service (Amazon SNS)
B. Amazon Simple Email Service (Amazon SES)
C. Amazon CloudWatch alerts
D. Amazon Simple Queue Service (Amazon SQS)''',
     'respuesta': 'D. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon SQS is a message queue service used by distributed applications to exchange messages through a polling model, and can be used to decouple sending and receiving components—without requiring each component to be concurrently available.',
     'referencia': 'https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html'},
    {'pregunta': 'A user is able to set up a master payer account to view consolidated billing reports through:',
     'opciones': '''A. AWS Budgets.
B. Amazon Macie.
C. Amazon QuickSight.
D. AWS Organizations.''',
     'respuesta': 'D. AWS Organizations.',
     'argumento': 'You can track the charges across multiple accounts and download the combined cost and usage data.',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html'}, #155
    {'pregunta': 'According to the AWS shared responsibility model, which task is the customer´s responsibility?',
     'opciones': '''A. Maintaining the infrastructure needed to run AWS Lambda
B. Updating the operating system of Amazon DynamoDB instances
C. Maintaining Amazon S3 infrastructure
D. Updating the guest operating system on Amazon EC2 instances''',
     'respuesta': 'D. Updating the guest operating system on Amazon EC2 instances',
     'argumento': 'According to the AWS shared responsibility model, updating the guest operating system on an Amazon EC2 instance is the customer´s responsibility. Therefore, the correct answer is D. AWS is responsible for the security of the cloud infrastructure, including the physical security of the data centers, the security of the hypervisor, and the security of the networking and storage infrastructure. However, the customer is responsible for the security of their own applications and data, including the guest operating system and any applications running on it. Other tasks that are the customer´s responsibility include securing access to AWS services and resources, configuring network security groups and firewalls, managing user access and permissions, and implementing security controls at the application layer. Maintenance of AWS services such as AWS Lambda, Amazon DynamoDB, and Amazon S3 is the responsibility of AWS, not the customer. ',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/#:~:text=Customers%20are%20responsible%20for%20managing,also%20extends%20to%20IT%20controls'},
    {'pregunta': 'A company wants to migrate a small website and database quickly from on-premises infrastructure to the AWS Cloud. The company has limited operational knowledge to perform the migration. Which AWS service supports this use case?',
     'opciones': '''A. Amazon EC2
B. Amazon Lightsail
C. Amazon S3
D. AWS Lambda''',
     'respuesta': 'B. Amazon Lightsail',
     'argumento': 'Lightsail instances are specifically engineered by AWS for web servers, developer environments, and small database use cases.',
     'referencia': 'https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-frequently-asked-questions-faq'},
    {'pregunta': 'A company is moving multiple applications to a single AWS account. The company wants to monitor the AWS Cloud costs incurred by each application. What can the company do to meet this requirement?',
     'opciones': '''A. Set up invoiced billing.
B. Use AWS Artifact.
C. Set budgets in Cost Explorer.
D. Create cost allocation tags.''',
     'respuesta': 'D. Create cost allocation tags.',
     'argumento': 'It’s also not possible to create custom budgets directly from AWS Cost Explorer',
     'referencia': 'https://www.cloudzero.com/blog/aws-budgets-vs-cost-explorer#:~:text=AWS%20cost%20tool.-,What%20Are%20The%20Differences%20Between%20AWS%20Budgets%20And%20Cost%20Explorer,costs%20and%20forecast%20future%20spending.'},
    {'pregunta': 'Which design principle is achieved by following the reliability pillar of the AWS Well-Architected Framework?',
     'opciones': '''A. Vertical scaling
B. Manual failure recovery
C. Testing recovery procedures
D. Changing infrastructure manually''',
     'respuesta': 'C. Testing recovery procedures',
     'argumento': 'The reliability pillar focuses on ensuring that a workload operates continuously and reliably, even in the face of failures. It emphasizes the implementation of mechanisms to automatically recover from failures, such as using redundancy, fault tolerance, and automated backup and restore processes. As part of this pillar, it is important to test recovery procedures regularly to validate their effectiveness and ensure they function as expected during actual failure scenarios. By conducting regular testing and simulations, organizations can identify and address any issues or gaps in their recovery procedures, improving the overall reliability of their workload.',
     'referencia': 'https://aws.amazon.com/blogs/apn/the-5-pillars-of-the-aws-well-architected-framework/'},
    {'pregunta': 'A user needs to quickly deploy a non-relational database on AWS. The user does not want to manage the underlying hardware or the database software. Which AWS service can be used to accomplish this?',
     'opciones': '''A. Amazon RDS
B. Amazon DynamoDB
C. Amazon Aurora
D. Amazon Redshift''',
     'respuesta': 'B. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is a fully managed NoSQL database service provided by AWS. It allows users to store and retrieve any amount of data and serves as a key-value and document database. DynamoDB takes care of the infrastructure management, including hardware provisioning, database setup, scaling, and patching, allowing users to focus on their application development.',
     'referencia': 'https://aws.amazon.com/dynamodb/features/'}, #160
    {'pregunta': 'Which task is an AWS responsibility when a workload is running in Amazon RDS?',
     'opciones': '''A. Creating the database table
B. Updating the database schema
C. Installing the database engine
D. Dropping the database records''',
     'respuesta': 'C. Installing the database engine',
     'argumento': 'Amazon RDS takes care of the underlying infrastructure and manages the installation, configuration, and patching of the database engine. Users can focus on managing their databases, including creating tables, updating the schema, and managing the data, while AWS handles the database engine administration.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html'},
    {'pregunta': 'A development team wants to publish and manage web services that provide REST APIs. Which AWS service will meet this requirement?',
     'opciones': '''A. AWS App Mesh
B. Amazon API Gateway
C. Amazon CloudFront
D. AWS Cloud Map''',
     'respuesta': 'B. Amazon API Gateway',
     'argumento': 'Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.',
     'referencia': 'https://aws.amazon.com/api-gateway/'},
    {'pregunta': 'A company has a social media platform in which users upload and share photos with other users. The company wants to identify and remove inappropriate photos. The company has no machine learning (ML) scientists and must build this detection capability with no ML expertise. Which AWS service should the company use to build this capability?',
     'opciones': '''A. Amazon SageMaker
B. Amazon Textract
C. Amazon Rekognition
D. Amazon Comprehend''',
     'respuesta': 'C. Amazon Rekognition',
     'argumento': 'Detect inappropriate content, Quickly and accurately identify unsafe or inappropriate content across image and video assets based on general or business-specific standards and practices.',
     'referencia': 'https://aws.amazon.com/rekognition/'},
    {'pregunta': 'Which responsibility belongs to AWS when a company hosts its databases on Amazon EC2 instances?',
     'opciones': '''A. Database backups
B. Database software patches
C. Operating system patches
D. Operating system installations.''',
     'respuesta': 'D. Operating system installations.',
     'argumento': 'When you choose to use EC2 for your database, you first have to provision the EC2 instance, which means you will use an AMI, containing the OS itself which is then installed by AWS to the EC2. All the other tasks are your responsibility.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/17/'},
    {'pregunta': 'A company wants to use Amazon S3 to store its legacy data. The data is rarely accessed. However, the data is critical and cannot be recreated. The data needs to be available for retrieval within seconds. Which S3 storage class meets these requirements MOST cost-effectively?',
     'opciones': '''A. S3 Standard
B. S3 One Zone-Infrequent Access (S3 One Zone-IA)
C. S3 Standard-Infrequent Access (S3 Standard-IA)
D. S3 Glacier''',
     'respuesta': 'C. S3 Standard-Infrequent Access (S3 Standard-IA)',
     'argumento': 'The S3 Standard - Infrequent Access type is used with data that is accessed less frequently, but requires fast access when needed. The S3 Standard - Infrequent Access type offers the level of high durability, high throughput, and low latency of S3 Standard, with a small storage charge per GB and recovery charge per GB. The combination of high performance and low cost makes S3 Standard - Infrequent Access the ideal choice for long-term storage, backup, and as a data store for disaster recovery archives. S3 storage classes can be configured at the object level, and a single bucket can contain objects stored in S3 Standard, S3 Smart Layers, S3 Standard - Infrequent Access, and S3 Single Zone - Infrequent Access. You can also use S3 lifecycle policies to automatically move objects between storage types without application changes.',
     'referencia': 'https://aws.amazon.com/es/s3/storage-classes/'}, #165
    {'pregunta': 'An online retail company wants to migrate its on-premises workload to AWS. The company needs to automatically handle a seasonal workload increase in a cost- effective manner. Which AWS Cloud features will help the company meet this requirement? (Choose two.)',
     'opciones': '''A. Cross-Region workload deployment
B. Pay-as-you-go pricing
C. Built-in AWS CloudTrail audit capabilities
D. Auto Scaling policies
E. Centralized logging''',
     'respuesta': '''B. Pay-as-you-go pricing
D. Auto Scaling policies''',
     'argumento': 'Pay-as-you-go pricing: With pay-as-you-go pricing, the company can scale its resources up or down based on demand during the seasonal workload increase. This allows the company to pay only for the resources it uses, helping to optimize costs.  Auto Scaling policies: Auto Scaling allows the company to automatically adjust the number of resources based on demand. By setting up Auto Scaling policies, the company can define rules to automatically add or remove resources to match the workload. This ensures that the company can handle the seasonal workload increase efficiently while minimizing costs during periods of lower demand.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/17/'},
    {'pregunta': 'Which AWS service helps developers use loose coupling and reliable messaging between microservices?',
     'opciones': '''A. Elastic Load Balancing
B. Amazon Simple Notification Service (Amazon SNS)
C. Amazon CloudFront
D. Amazon Simple Queue Service (Amazon SQS)''',
     'respuesta': 'D. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon SQS is a fully managed message queuing service that enables decoupling and asynchronous communication between microservices. It provides reliable message delivery and ensures that messages are processed in a scalable and fault-tolerant manner. By using SQS, developers can implement a publish-subscribe pattern or a message queue pattern to enable loosely coupled communication between microservices.',
     'referencia': 'https://aws.amazon.com/sqs/#:~:text=Amazon%20SQS%20provides%20a%20simple%20and%20reliable%20way%20for%20customers%20to%20decouple%20and%20connect%20components%20(microservices)%20together%20using%20queues.'},
    {'pregunta': 'A company needs to build an application that uses AWS services. The application will be delivered to residents in European Counties. The company must abide by regional regulatory requirements. Which AWS service or program should the company use to determine which AWS services meet the regional requirements?',
     'opciones': '''A. AWS Audit Manager
B. AWS Shield
C. AWS Compliance Program
D. AWS Artifact''',
     'respuesta': 'C. AWS Compliance Program',
     'argumento': 'The AWS Compliance Program provides information and resources to help customers understand how AWS services align with specific compliance requirements in different regions. It includes details on the compliance programs and certifications that AWS has obtained, such as GDPR, HIPAA, ISO, and more. The AWS Compliance Program provides comprehensive information about regional requirements and helps customers ensure that their applications meet the necessary regulatory standards.',
     'referencia': 'https://aws.amazon.com/compliance/programs/'},
    {'pregunta': 'A company needs to implement identity management for a fleet of mobile apps that are running in the AWS Cloud. Which AWS service will meet this requirement',
     'opciones': '''A. Amazon Cognito
B. AWS Security Hub
C. AWS Shield
D. AWS WAF''',
     'respuesta': 'A. Amazon Cognito',
     'argumento': 'Amazon Cognito helps you implement customer identity and access management (CIAM) into your web and mobile applications. You can quickly add user authentication and access control to your applications in minutes.',
     'referencia': 'https://aws.amazon.com/cognito/'},
    {'pregunta': 'A company needs an Amazon EC2 instance for a rightsized database server that must run constantly for 1 year. Which EC2 instance purchasing option will meet these requirements MOST cost-effectively?',
     'opciones': '''A. Standard Reserved Instance
B. Convertible Reserved Instance
C. On-Demand Instance
D. Spot Instance''',
     'respuesta': 'A. Standard Reserved Instance',
     'argumento': 'Standard Reserved Instances typically provide the highest discount levels. One-year Standard Reserved Instances provide a similar discount to three-year Convertible Reserved Instances.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/standard-vs.-convertible-offering-classes.html'}, #170
    {'pregunta': 'A company has multiple applications and is now building a new multi-tier application. The company will host the new application on Amazon EC2 instances. The company wants the network routing and traffic between the various applications to follow the security principle of least privilege. Which AWS service or feature should the company use to enforce this principle?',
     'opciones': '''A. Security groups
B. AWS Shield
C. AWS Global Accelerator
D. AWS Direct Connect gateway''',
     'respuesta': 'A. Security groups',
     'argumento': 'A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don´t specify a security group, Amazon EC2 uses the default security group for the VPC. You can add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time. New and modified rules are automatically applied to all instances that are associated with the security group. When Amazon EC2 decides whether to allow traffic to reach an instance, it evaluates all of the rules from all of the security groups that are associated with the instance.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html'},
    {'pregunta': 'A company´s web application requires AWS credentials and authorizations to use an AWS service. Which IAM entity should the company use as best practice?',
     'opciones': '''A. IAM role
B. IAM user
C. IAM group
D. IAM multi-factor authentication (MFA)''',
     'respuesta': 'A. IAM role',
     'argumento': 'We recommend using IAM roles for human users and workloads that access your AWS resources so that they use temporary credentials. However, for scenarios in which you need an IAM user or root user in your account, require MFA for additional security. With MFA, users have a device that generates a response to an authentication challenge. Each user´s credentials and device-generated response are required to complete the sign-in process.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#enable-mfa-for-privileged-users'},
    {'pregunta': 'A company is creating a document that defines the operating system patch routine for all the company´s systems. Which AWS resources should the company include in this document? (Choose two.)',
     'opciones': '''A. Amazon EC2 instances
B. AWS Lambda functions
C. AWS Fargate tasks
D. Amazon RDS instances
E. Amazon Elastic Container Service (Amazon ECS) instances''',
     'respuesta': '''A. Amazon EC2 instances. 
D. Amazon RDS instances''',
     'argumento': 'A. Amazon EC2 instances: EC2 instances are virtual servers in the cloud, and they often run the company´s systems and applications. Including EC2 instances in the patch routine document ensures that the operating systems on these instances are regularly updated and patched for security and performance reasons. D. Amazon RDS instances: Amazon RDS (Relational Database Service) provides managed database services. If the company is using RDS instances for their databases, it is important to include them in the patch routine document to ensure that the database operating systems receive regular updates and security patches.',
     'referencia': 'https://aws.amazon.com/blogs/industries/automate-patching-by-replacing-amazon-ecs-container-instances/'},
    {'pregunta': 'Which AWS service or feature gives a company the ability to control incoming traffic and outgoing traffic for Amazon EC2 instances?',
     'opciones': '''A. Security groups
B. Amazon Route 53
C. AWS Direct Connect
D. Amazon VPC''',
     'respuesta': 'A. Security groups',
     'argumento': 'A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don´t specify a security group, Amazon EC2 uses the default security group for the VPC. You can add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time. New and modified rules are automatically applied to all instances that are associated with the security group. When Amazon EC2 decides whether to allow traffic to reach an instance, it evaluates all of the rules from all of the security groups that are associated with the instance.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html'},
    {'pregunta': 'A company is starting to build its infrastructure in the AWS Cloud. The company wants access to technical support during business hours. The company also wants general architectural guidance as teams build and test new applications. Which AWS Support plan will meet these requirements at the LOWEST cost?',
     'opciones': '''A. AWS Basic Support
B. AWS Developer Support
C. AWS Business Support
D. AWS Enterprise Support''',
     'respuesta': 'B. AWS Developer Support',
     'argumento': 'AWS Developer Support is designed for developers and technical teams who need access to technical support during business hours. It provides a cost-effective support option with access to AWS Support engineers via email during business hours. This plan is suitable for companies that require basic technical assistance and general architectural guidance as they build and test new applications.',
     'referencia': 'https://www.amazonaws.cn/en/support/compare-plans/'}, #175
    {'pregunta': 'A company is migrating its public website to AWS. The company wants to host the domain name for the website on AWS. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. AWS Lambda
B. Amazon Route 53
C. Amazon CloudFront
D. AWS Direct Connect''',
     'respuesta': 'B. Amazon Route 53',
     'argumento': 'Amazon Route 53 is a scalable and highly available Domain Name System (DNS) web service provided by AWS. It allows you to register and manage domain names and perform DNS routing for your applications. Route 53 provides various DNS management features, including domain registration, DNS routing policies, and health checks. In the case of hosting the domain name for the company´s website on AWS, Amazon Route 53 can be used to register the domain name, configure the DNS settings, and point the domain to the appropriate AWS resources, such as the website hosted on Amazon S3, Amazon EC2 instances, or load balancers.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/18/'},
    {'pregunta': 'A company needs to evaluate its AWS environment and provide best practice recommendations in five categories: cost, performance, service limits, fault tolerance, and security. Which AWS service can the company use to meet these requirements?',
     'opciones': '''A. AWS Shield
B. AWS WAF
C. AWS Trusted Advisor
D. AWS Service Catalog''',
     'respuesta': 'C. AWS Trusted Advisor',
     'argumento': 'AWS Trusted Advisor is used to evaluate its AWS environment and provide best practice recommendations in five categories: cost, performance, service limits, fault tolerance, and security.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/#:~:text=Advisor%20(11%3A45)-,Benefits,-Checks%20from%20Trusted'},
    {'pregunta': 'Which AWS service provides the capability to view end-to-end performance metrics and troubleshoot distributed applications?',
     'opciones': '''A. AWS Cloud9
B. AWS CodeStar
C. AWS Cloud Map
D. AWS X-Ray''',
     'respuesta': 'D. AWS X-Ray',
     'argumento': 'AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. X-Ray provides an end-to-end view of requests as they travel through your application, and shows a map of your application’s underlying components.',
     'referencia': 'https://aws.amazon.com/xray/faqs/'},
    {'pregunta': 'Which cloud computing benefit does AWS demonstrate with its ability to offer lower variable costs as a result of high purchase volumes?',
     'opciones': '''A. Pay-as-you-go pricing
B. High availability
C. Global reach
D. Economies of scale''',
     'respuesta': 'D. Economies of scale',
     'argumento': 'Benefit from massive economies of scale – By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html#:~:text=Benefit%20from%20massive,you%2Dgo%20prices.'},
    {'pregunta': 'Which AWS service provides threat detection by monitoring for malicious activities and unauthorized actions to protect AWS accounts, workloads, and data that is stored in Amazon S3?',
     'opciones': '''A. AWS Shield
B. AWS Firewall Manager
C. Amazon GuardDuty
D. Amazon Inspector''',
     'respuesta': 'C. Amazon GuardDuty',
     'argumento': 'GuardDuty is an intelligent threat detection service that continuously monitors your AWS accounts, Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS Lambda functions, Amazon Elastic Kubernetes Service (Amazon EKS) clusters, Amazon Aurora login activity, and data stored in Amazon Simple Storage Service (Amazon S3) for malicious activity. ',
     'referencia': 'https://aws.amazon.com/guardduty/faqs/'}, #180
    {'pregunta': 'Which AWS service can a company use to store and manage Docker images?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon Kinesis Data Streams
C. Amazon Elastic Container Registry (Amazon ECR)
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'C. Amazon Elastic Container Registry (Amazon ECR)',
     'argumento': 'Amazon Elastic Container Registry (Amazon ECR) is a fully managed container registry service provided by AWS. It allows you to store, manage, and deploy Docker container images. With Amazon ECR, you can securely store your container images and easily integrate them with other AWS services, such as Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS), for running containerized applications.',
     'referencia': 'https://aws.amazon.com/docker/#:~:text=AWS%20provides%20Amazon%20Elastic%20Container,and%20quickly%20retrieving%20Docker%20images.'},
    {'pregunta': 'A company needs an automated security assessment report that will identify unintended network access to Amazon EC2 instances. The report also must identify operating system vulnerabilities on those instances. Which AWS service or feature should the company use to meet this requirement?',
     'opciones': '''A. AWS Trusted Advisor
B. Security groups
C. Amazon Macie
D. Amazon Inspector''',
     'respuesta': 'D. Amazon Inspector',
     'argumento': 'Amazon Inspector is an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2), AWS Lambda functions, and container workloads for software vulnerabilities and unintended network exposure.',
     'referencia': 'https://aws.amazon.com/inspector/faqs/?nc=sn&loc=6'},
    {'pregunta': 'A global company is building a simple time-tracking mobile app. The app needs to operate globally and must store collected data in a database. Data must be accessible from the AWS Region that is closest to the user. What should the company do to meet these data storage requirements with the LEAST amount of operational overhead?',
     'opciones': '''A. Use Amazon EC2 in multiple Regions to host separate databases
B. Use Amazon RDS cross-Region replication
C. Use Amazon DynamoDB global tables
D. Use AWS Database Migration Service (AWS DMS)''',
     'respuesta': 'C. Use Amazon DynamoDB global tables',
     'argumento': 'Global tables build on the global Amazon DynamoDB footprint to provide you with a fully managed, multi-Region, and multi-active database that delivers fast, local, read and write performance for massively scaled, global applications. Global tables replicate your DynamoDB tables automatically across your choice of AWS Regions.',
     'referencia': 'https://aws.amazon.com/dynamodb/global-tables/'},
    {'pregunta': 'Which of the following are economic advantages of the AWS Cloud? (Choose two.)',
     'opciones': '''A. Increased workforce productivity
B. Decreased need to encrypt user data
C. Manual compliance audits
D. Simplified total cost of ownership (TCO) accounting
E. Faster product launches''',
     'respuesta': '''D. Simplified total cost of ownership (TCO) accounting. 
E. Faster product launches''',
     'argumento': 'D. Simplified total cost of ownership (TCO) accounting: The AWS Cloud offers a pay-as-you-go pricing model, where users only pay for the resources they consume. This eliminates the need for large upfront capital investments and allows for more accurate and predictable cost management. E. Faster product launches: The AWS Cloud provides a wide range of pre-configured services and resources that can be quickly provisioned and scaled as needed. This allows companies to accelerate their product development and deployment cycles, leading to faster time-to-market and potential cost savings.',
     'referencia': 'https://aws.amazon.com/economics/'},
    {'pregunta': 'Which controls does the customer fully inherit from AWS in the AWS shared responsibility model?',
     'opciones': '''A. Patch management controls
B. Awareness and training controls
C. Physical and environmental controls
D. Configuration management controls''',
     'respuesta': 'C. Physical and environmental controls',
     'argumento': 'In the AWS shared responsibility model, the customer fully inherits physical and environmental controls from AWS. This means that AWS is responsible for the security and management of the underlying infrastructure, including the data centers, networking, and power systems. AWS implements stringent physical and environmental controls to ensure the security and availability of their infrastructure.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'}, #185
    {'pregunta': 'Which task is a customer´s responsibility, according to the AWS shared responsibility model?',
     'opciones': '''A. Management of the guest operating systems
B. Maintenance of the configuration of infrastructure devices
C. Management of the host operating systems and virtualization
D. Maintenance of the software that powers Availability Zones''',
     'respuesta': 'A. Management of the guest operating systems',
     'argumento': 'The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/#:~:text=The%20customer%20assumes%20responsibility%20and%20management%20of%20the%20guest%20operating%20system%20(including%20updates%20and%20security%20patches)%2C%20other%20associated%20application%20software%20as%20well%20as%20the%20configuration%20of%20the%20AWS%20provided%20security%20group%20firewall.'},
    {'pregunta': 'A company needs to deliver new website features quickly in an iterative manner to minimize the time to market. Which AWS Cloud concept does this requirement represent?',
     'opciones': '''A. Reliability
B. Elasticity
C. Agility
D. High availability''',
     'respuesta': 'C. Agility',
     'argumento': 'Agility refers to the ability to rapidly and easily adapt to changing business needs and market demands. In the context of AWS, it means having the ability to quickly deploy and scale resources, implement changes, and iterate on applications or services. By leveraging AWS services and features, companies can take advantage of the cloud´s flexibility and automation capabilities to accelerate their development and deployment cycles, allowing them to bring new features and updates to market more efficiently.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/19/'},
    {'pregunta': 'A company wants to increase its ability to recover its infrastructure in the case of a natural disaster. Which pillar of the AWS Well-Architected Framework does this ability represent?',
     'opciones': '''A. Cost optimization
B. Performance efficiency
C. Reliability
D. Security''',
     'respuesta': 'C. Reliability',
     'argumento': 'Automatically recover from failure: By monitoring a workload for key performance indicators (KPIs), you can trigger automation when a threshold is breached. These KPIs should be a measure of business value, not of the technical aspects of the operation of the service. This allows for automatic notification and tracking of failures, and for automated recovery processes that work around or repair the failure. With more sophisticated automation, it’s possible to anticipate and remediate failures before they occur.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.reliability.en.html#:~:text=Automatically%20recover%20from,before%20they%20occur.'},
    {'pregunta': 'Which AWS service tracks API calls and user activity?',
     'opciones': '''A. AWS Organizations
B. AWS Config
C. Amazon CloudWatch
D. AWS CloudTrail''',
     'respuesta': 'D. AWS CloudTrail',
     'argumento': 'AWS CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs, continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.',
     'referencia': 'https://aws.amazon.com/cloudtrail/faqs/'},
    {'pregunta': 'Which AWS service, feature, or tool uses machine learning to continuously monitor cost and usage for unusual cloud spending?',
     'opciones': '''A. Amazon Lookout for Metrics
B. AWS Budgets
C. Amazon CloudWatch
D. AWS Cost Anomaly Detection''',
     'respuesta': 'D. AWS Cost Anomaly Detection',
     'argumento': 'AWS Cost Anomaly Detection is an AWS cost management feature that uses machine learning to continually monitor your cost and usage to detect unusual spends.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-cloud-financial-management-services-and-tools.html'}, #190
    {'pregunta': 'A company deployed an application on an Amazon EC2 instance. The application ran as expected for 6 months in the past week, users have reported latency issues. A system administrator found that the CPU utilization was at 100% during business hours. The company wants a scalable solution to meet demand. Which AWS service or feature should the company use to handle the load for its application during periods of high demand?',
     'opciones': '''A. Auto Scaling groups
B. AWS Global Accelerator
C. Amazon Route 53
D. An Elastic IP address''',
     'respuesta': 'A. Auto Scaling groups',
     'argumento': 'An Auto Scaling group starts by launching enough instances to meet its desired capacity. It maintains this number of instances by performing periodic health checks on the instances in the group. The Auto Scaling group continues to maintain a fixed number of instances even if an instance becomes unhealthy. If an instance becomes unhealthy, the group terminates the unhealthy instance and launches another instance to replace it.',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html'},
    {'pregunta': 'A company wants to migrate to AWS and use the same security software it uses on premises. The security software vendor offers its security software as a service on AWS. Where can the company purchase the security solution?',
     'opciones': '''A. AWS Partner Solutions Finder
B. AWS Support Center
C. AWS Management Console
D. AWS Marketplace''',
     'respuesta': 'D. AWS Marketplace',
     'argumento': 'The AWS Marketplace is an online store that offers a wide selection of third-party software, including security solutions, that can be used on AWS. It provides a platform for customers to find, compare, and purchase software solutions that meet their specific needs. Vendors can list their software offerings on the AWS Marketplace, making it a convenient and centralized location for customers to discover and acquire the software they require.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/20/'},
    {'pregunta': 'A company is generating large sets of critical data in its on-premises data center. The company needs to securely transfer the data to AWS for processing. These transfers must occur daily over a dedicated connection. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS Backup
B. AWS DataSync
C. AWS Direct Connect
D. AWS Snowball''',
     'respuesta': 'C. AWS Direct Connect',
     'argumento': 'AWS Direct Connect provides a dedicated network connection from the company´s on-premises environment to AWS. It establishes a private and secure connection that bypasses the public internet, ensuring reliable and low-latency data transfers. With AWS Direct Connect, the company can transfer data directly from its data center to AWS without going through the internet, resulting in improved security and data transfer performance.',
     'referencia': 'https://aws.amazon.com/directconnect/'},
    {'pregunta': 'A company wants to run production workloads on AWS. The company wants access to technical support from engineers 24 hours a day, 7 days a week. The company also wants access to the AWS Health API and contextual architectural guidance for business use cases. The company has a strong IT support team and does not need concierge support. Which AWS Support plan will meet these requirements at the LOWEST cost?',
     'opciones': '''A. AWS Basic Support
B. AWS Developer Support
C. AWS Business Support
D. AWS Enterprise Support''',
     'respuesta': 'C. AWS Business Support',
     'argumento': 'AWS Business Support provides 24/7 access to AWS Trusted Advisor, AWS Infrastructure Event Management, and the AWS Health API, which are the features that the company needs. Business Support also includes access to AWS Support engineers during business hours, which should be sufficient given the strong IT support team the company already has in place. Additionally, Business Support provides architectural guidance for specific business use cases, which can be useful for optimizing the company´s use of AWS.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/business/'},
    {'pregunta': 'Which of the following is a managed AWS service that is used specifically for extract, transform, and load (ETL) data?',
     'opciones': '''A. Amazon Athena
B. AWS Glue
C. Amazon S3
D. AWS Snowball Edge''',
     'respuesta': 'B. AWS Glue',
     'argumento': 'AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easier to discover, prepare, and combine data for analytics, machine learning (ML), and application development.',
     'referencia': 'https://aws.amazon.com/it/what-is/etl/#:~:text=AWS%20Glue%20is%20a%20fully,ML)%2C%20and%20application%20development.'}, #195
    {'pregunta': 'Which of the following actions are controlled with AWS Identity and Access Management (IAM)? (Choose two.)',
     'opciones': '''A. Control access to AWS service APIs and to other specific resources.
B. Provide intelligent threat detection and continuous monitoring.
C. Protect the AWS environment using multi-factor authentication (MFA).
D. Grant users access to AWS data centers.
E. Provide firewall protection for applications from common web attacks.''',
     'respuesta': '''A. Control access to AWS service APIs and to other specific resources.
C. Protect the AWS environment using multi-factor authentication (MFA).''',
     'argumento': 'A. IAM allows you to manage permissions and access to various AWS service APIs and specific resources such as Amazon S3 buckets, EC2 instances, and more. IAM provides fine-grained control over what actions users and roles can perform within the AWS environment. C. IAM supports multi-factor authentication (MFA), which adds an extra layer of security to AWS accounts. MFA requires users to provide two or more forms of identification (e.g., password and a temporary authentication code from a virtual MFA device or hardware MFA token) before they can access AWS resources.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/20/'},
    {'pregunta': 'Which of the following are shared controls that apply to both AWS and the customer, according to the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Resource configuration management
B. Network data integrity
C. Employee awareness and training
D. Physical and environmental security
E. Replacement and disposal of disk drives''',
     'respuesta': '''A. Resource configuration management. 
C. Employee awareness and training''',
     'argumento': 'A. Resource configuration management: Both AWS and the customer share the responsibility of properly configuring and managing the resources they use in the AWS environment. C. Employee awareness and training: Both AWS and the customer share the responsibility of ensuring that employees are aware of and trained in security best practices and compliance requirements.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'What information is found on an AWS Identity and Access Management (IAM) credential report? (Choose two.)',
     'opciones': '''A. The date and time when an IAM user's password was last used to sign in to the AWS Management Console.
B. The type of multi-factor authentication (MFA) device assigned to an IAM user.
C. The User-Agent browser identifier for each IAM user currently logged in.
D. Whether multi-factor authentication (MFA) has been enabled for an IAM user.
E. The number of incorrect login attempts by each IAM user in the previous 30 days.''',
     'respuesta': '''A. The date and time when an IAM user´s password was last used to sign in to the AWS Management Console. 
D. Whether multi-factor authentication (MFA) has been enabled for an IAM user.''',
     'argumento': 'The IAM credential report provides details about the IAM users in an AWS account, including their access keys, passwords, MFA devices, and various other security-related information. However, the report does not include information such as the type of MFA device assigned to an IAM user, the User-Agent browser identifier for each logged-in IAM user, or the number of incorrect login attempts.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html#id_credentials_understanding_the_report_format'},
    {'pregunta': 'What is the LEAST expensive AWS Support plan that contains a full set of AWS Trusted Advisor best practice checks?',
     'opciones': '''A. AWS Enterprise Support
B. AWS Business Support
C. AWS Developer Support
D. AWS Basic Support''',
     'respuesta': 'B. AWS Business Support',
     'argumento': 'AWS Basic Support and AWS Developer Support customers can access core security checks and checks for service quotas. AWS Business Support and AWS Enterprise Support customers can access all checks, including cost optimization, security, fault tolerance, performance, and service quotas.',
     'referencia': 'https://www.amazonaws.cn/en/support/compare-plans/'},
    {'pregunta': 'Which AWS service provides domain registration, DNS routing, and service health checks?',
     'opciones': '''A. AWS Direct Connect
B. Amazon Route 53
C. Amazon CloudFront
D. Amazon API Gateway''',
     'respuesta': 'B. Amazon Route 53',
     'argumento': 'Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Route 53 connects user requests to internet applications running on AWS or on-premises.',
     'referencia': 'https://aws.amazon.com/route53/'}, #200
    {'pregunta': 'A bank needs to store recordings of calls made to its contact center for 6 years. The recordings must be accessible within 48 hours from the time they are requested. Which AWS service will provide a secure and cost-effective solution for retaining these files?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon S3 Glacier
C. Amazon Connect
D. Amazon ElastiCache''',
     'respuesta': 'B. Amazon S3 Glacier',
     'argumento': 'To save even more on long-lived archive storage such as compliance archives and digital media preservation, choose S3 Glacier Deep Archive, the lowest cost storage in the cloud with data retrieval within twelve hours.',
     'referencia': 'https://aws.amazon.com/s3/storage-classes/glacier/'},
    {'pregunta': 'Which AWS service should be used to migrate a company´s on-premises MySQL database to Amazon RDS?',
     'opciones': '''A. AWS Direct Connect
B. AWS Server Migration Service (AWS SMS)
C. AWS Database Migration Service (AWS DMS)
D. AWS Schema Conversion Tool (AWS SCT)''',
     'respuesta': 'C. AWS Database Migration Service (AWS DMS)',
     'argumento': 'AWS Database Migration Service (AWS DMS) is a managed migration and replication service that helps move your database and analytics workloads to AWS quickly, securely, and with minimal downtime and zero data loss. AWS DMS supports migration between 20-plus database and analytics engines, such as Oracle to Amazon Aurora MySQL-Compatible Edition, MySQL to Amazon Relational Database (RDS) for MySQL, Microsoft SQL Server to Amazon Aurora PostgreSQL-Compatible Edition, MongoDB to Amazon DocumentDB (with MongoDB compatibility), Oracle to Amazon Redshift, and Amazon Simple Storage Service (S3).',
     'referencia': 'https://aws.amazon.com/dms/'},
    {'pregunta': 'Which benefits does a company gain when the company moves from on-premises IT architecture to the AWS Cloud? (Choose two.)',
     'opciones': '''A. Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement
B. Elimination of the need for trained IT staff
C. Automatic security configuration of all applications that are migrated to the cloud
D. Elimination of the need for disaster recovery planning
E. Faster deployment of new features and applications''',
     'respuesta': '''A. Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement.
E. Faster deployment of new features and applications''',
     'argumento': 'A. Reduced or eliminated tasks for hardware troubleshooting, capacity planning, and procurement: With the AWS Cloud, companies can offload the responsibility of managing hardware infrastructure, including troubleshooting issues, planning for capacity needs, and procuring new hardware. AWS manages the underlying infrastructure, allowing companies to focus on their core business. E. Faster deployment of new features and applications: AWS provides a wide range of services and tools that enable companies to quickly deploy and scale applications. The cloud infrastructure allows for agility and faster time to market, as companies can easily provision resources and take advantage of managed services for various functionalities.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/21/'},
    {'pregunta': 'Which of the following is a benefit of decoupling an AWS Cloud architecture?',
     'opciones': '''A. Reduced latency
B. Ability to upgrade components independently
C. Decreased costs
D. Fewer components to manage''',
     'respuesta': 'B. Ability to upgrade components independently',
     'argumento': 'The benefit of decoupling an AWS Cloud architecture is the ability to upgrade components independently. When components are decoupled, they are not tightly coupled or dependent on each other, allowing for independent upgrades or changes to specific components without affecting the entire system. This provides flexibility and agility in managing and evolving the architecture over time.',
     'referencia': 'https://www.cloudamqp.com/blog/why-is-application-decoupling-a-good-thing.html#:~:text=A%20decoupled%20application%20architecture%20allows,and%20unaware%20of%20each%20other.'},
    {'pregunta': 'Which task is the responsibility of the customer according to the AWS shared responsibility model?',
     'opciones': '''A. Maintain the security of the hardware that runs Amazon EC2 instances.
B. Patch the guest operating system of Amazon EC2 instances.
C. Protect the security of the AWS global infrastructure.
D. Patch Amazon RDS software.''',
     'respuesta': 'B. Patch the guest operating system of Amazon EC2 instances.',
     'argumento': 'Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'}, #205
    {'pregunta': 'Which AWS Organizations feature can be used to track charges across multiple accounts and report the combined cost?',
     'opciones': '''A. Service control policies (SCPs)
B. Cost Explorer
C. Consolidated billing
D. AWS Identity and Access Management (IAM)''',
     'respuesta': 'C. Consolidated billing',
     'argumento': 'You can use the consolidated billing feature in AWS Organizations to consolidate billing and payment for multiple AWS accounts or multiple Amazon Web Services India Private Limited (AWS India) accounts',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html'},
    {'pregunta': 'Which of the following is a cloud benefit that AWS offers to its users?',
     'opciones': '''A. The ability to configure AWS data center hypervisors
B. The ability to purchase hardware in advance of increased traffic
C. The ability to deploy to AWS on a global scale
D. Compliance audits for user IT environments''',
     'respuesta': 'C. The ability to deploy to AWS on a global scale',
     'argumento': 'Go global in minutes – Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at minimal cost.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'An ecommerce company has migrated its IT infrastructure from an on-premises data center to the AWS Cloud. Which cost is the company´s direct responsibility?',
     'opciones': '''A. Cost of application software licenses
B. Cost of the hardware infrastructure on AWS
C. Cost of power for the AWS servers
D. Cost of physical security for the AWS data center''',
     'respuesta': 'A. Cost of application software licenses',
     'argumento': 'The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'What are the five pillars of the AWS Well-Architected Framework?',
     'opciones': '''A. Encryption, documentation, speed, hybrid design, and cost optimization
B. Containerization, cost margins, globalization, marketplace, and developer operations
C. Network, compute, storage, security, and developer operations
D. Operational excellence, reliability, performance efficiency, security, and cost optimization''',
     'respuesta': 'D. Operational excellence, reliability, performance efficiency, security, and cost optimization',
     'argumento': 'Operational excellence - Focuses on operational practices that allow organizations to run their workloads efficiently, gain insights into their operations, and continuously improve processes and procedures. Reliability - Focuses on the ability to recover from failures and meet business continuity objectives by designing systems that can automatically recover from infrastructure or service disruptions. Performance efficiency - Focuses on using resources efficiently to meet system requirements, including selecting the right resource types and sizes and optimizing performance as demands change. Security - Focuses on protecting information, systems, and assets while delivering business value through risk assessments, data protection mechanisms, and implementing various security controls. Cost optimization - Focuses on avoiding unnecessary costs by optimizing resource usage, selecting the right pricing models, and analyzing spending patterns to ensure cost-effectiveness.',
     'referencia': 'https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework/'},
    {'pregunta': 'A company accepts enrollment applications on handwritten paper forms. The company uses a manual process to enter the form data into its backend systems. The company wants to automate the process by scanning the forms and capturing the enrollment data from scanned PDF files. Which AWS service should the company use to build this process ',
     'opciones': '''A. Amazon Rekognition
B. Amazon Textract
C. Amazon Transcribe
D. Amazon Comprehend''',
     'respuesta': 'B. Amazon Textract',
     'argumento': 'Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, and data from scanned documents. It goes beyond simple optical character recognition (OCR) to identify, understand, and extract data from forms and tables.',
     'referencia': 'https://aws.amazon.com/textract/'}, #210
    {'pregunta': 'Which AWS service should a company use to organize, characterize, and search large numbers of images?',
     'opciones': '''A. Amazon Transcribe
B. Amazon Rekognition
C. Amazon Aurora
D. Amazon QuickSight''',
     'respuesta': 'B. Amazon Rekognition',
     'argumento': 'Searchable image and video libraries – Amazon Rekognition makes images and stored videos searchable so you can discover objects and scenes that appear within them',
     'referencia': 'https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html'},
    {'pregunta': 'An ecommerce company wants to use Amazon EC2 Auto Scaling to add and remove EC2 instances based on CPU utilization. Which AWS service or feature can initiate an Amazon EC2 Auto Scaling action to achieve this goal?',
     'opciones': '''A. Amazon Simple Queue Service (Amazon SQS)
B. Amazon Simple Notification Service (Amazon SNS)
C. AWS Systems Manager
D. Amazon CloudWatch alarm''',
     'respuesta': 'D. Amazon CloudWatch alarm',
     'argumento': 'Amazon EC2 Auto Scaling supports the following types of dynamic scaling policies: Target tracking scaling—Increase and decrease the current capacity of the group based on a Amazon CloudWatch metric and a target value. It works similar to the way that your thermostat maintains the temperature of your home—you select a temperature and the thermostat does the rest',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html'},
    {'pregunta': 'A company wants to host a private version control system for its application code in the AWS Cloud. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. AWS CodePipeline
B. AWS CodeStar
C. AWS CodeCommit
D. AWS CodeDeploy''',
     'respuesta': 'C. AWS CodeCommit',
     'argumento': 'AWS CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories. It makes it easy for teams to securely collaborate on code with contributions encrypted in transit and at rest.',
     'referencia': 'https://aws.amazon.com/codecommit/#:~:text=AWS%20CodeCommit%20is%20a%20secure,in%20transit%20and%20at%20rest.'},
    {'pregunta': 'Which AWS service or tool can a company set up to send notifications that a custom spending threshold has been reached or exceeded?',
     'opciones': '''A. AWS Budgets
B. AWS Trusted Advisor
C. AWS CloudTrail
D. AWS Support''',
     'respuesta': 'A. AWS Budgets',
     'argumento': 'With AWS Budgets, set custom budgets to track your costs and usage, and respond quickly to alerts received from email or SNS notifications if you exceed your threshold.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-budgets/'},
    {'pregunta': 'Which AWS service is used to host static websites?',
     'opciones': '''A. Amazon S3
B. Amazon Elastic Block Store (Amazon EBS)
C. AWS CloudFormation
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'A. Amazon S3',
     'argumento': 'You can use Amazon S3 to host a static website. On a static website, individual webpages include static content. They might also contain client-side scripts.By contrast, a dynamic website relies on server-side processing, including server-side scripts, such as PHP, JSP, or ASP.NET. Amazon S3 does not support server-side scripting, but AWS has other resources for hosting dynamic websites',
     'referencia': 'https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html'}, #215
    {'pregunta': 'Which AWS service contains built-in engines to protect web applications that run in the cloud from SQL injection attacks and cross-site scripting?',
     'opciones': '''A. AWS WAF
B. AWS Shield Advanced
C. Amazon GuardDuty
D. Amazon Detective''',
     'respuesta': 'A. AWS WAF',
     'argumento': 'AWS WAF is a web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) web requests based on conditions that you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and cross-site scripting.',
     'referencia': 'https://aws.amazon.com/waf/faqs/#:~:text=AWS%20WAF%20helps%20protects%20your,that%20contain%20particular%20request%20headers'},
    {'pregunta': 'A company owns per-core software licenses. Which Amazon EC2 instance purchasing option must the company use for this license type?',
     'opciones': '''A. Reserved Instances
B. Dedicated Hosts
C. Spot Instances
D. Dedicated Instances''',
     'respuesta': 'B. Dedicated Hosts',
     'argumento': 'Dedicated Hosts allow you to use your existing per-socket, per-core, or per-VM software licenses, including Windows Server, SQL Server, SUSE Linux Enterprise Server, Red Hat Enterprise Linux, or other software licenses that are bound to VMs, sockets, or physical cores, subject to your license terms.',
     'referencia': 'https://aws.amazon.com/ec2/dedicated-hosts/'},
    {'pregunta': 'A company needs to set up user authentication for a new application. Users must be able to sign in directly with a user name and password, or through a third- party provider. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS Single Sign-On
B. AWS Signer
C. Amazon Cognito
D. AWS Directory Service''',
     'respuesta': 'C. Amazon Cognito',
     'argumento': 'Amazon Cognito is an identity platform for web and mobile apps. It’s a user directory, an authentication server, and an authorization service for OAuth 2.0 access tokens and AWS credentials. With Amazon Cognito, you can authenticate and authorize users from the built-in user directory, from your enterprise directory, and from consumer identity providers like Google and Facebook.',
     'referencia': 'https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html'},
    {'pregunta': 'A company´s IT team is managing MySQL database server clusters. The IT team has to patch the database and take backup snapshots of the data in the clusters. The company wants to move this workload to AWS so that these tasks will be completed automatically. What should the company do to meet these requirements?',
     'opciones': '''A. Deploy MySQL database server clusters on Amazon EC2 instances.
B. Use Amazon RDS with a MySQL database.
C. Use an AWS CloudFormation template to deploy MySQL database servers on Amazon EC2 instances.
D. Migrate all the MySQL database data to Amazon S3.''',
     'respuesta': 'B. Use Amazon RDS with a MySQL database.',
     'argumento': 'Amazon RDS for MySQL frees you up to focus on application development by managing time-consuming database administration tasks, including backups, upgrades, software patching, performance improvements, monitoring, scaling, and replication.',
     'referencia': 'https://aws.amazon.com/rds/mysql/'},
    {'pregunta': 'What is the primary use case for Amazon GuardDuty?',
     'opciones': '''A. Prevention of DDoS attacks
B. Protection against SQL injection attacks
C. Automatic monitoring for threats to AWS workloads
D. Automatic provisioning of AWS resources''',
     'respuesta': 'C. Automatic monitoring for threats to AWS workloads',
     'argumento': 'Continuously monitor your AWS accounts, instances, serverless and container workloads, users, databases, and storage for potential threats. Amazon GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and delivers detailed security findings for visibility and remediation.',
     'referencia': 'https://aws.amazon.com/guardduty/'}, #220
    {'pregunta': 'Which statements explain the business value of migration to the AWS Cloud? (Choose two.)',
     'opciones': '''A. The migration of enterprise applications to the AWS Cloud makes these applications automatically available on mobile devices.
B. AWS availability and security provide the ability to improve service level agreements (SLAs) while reducing risk and unplanned downtime.
C. Companies that migrate to the AWS Cloud eliminate the need to plan for high availability and disaster recovery.
D. Companies that migrate to the AWS Cloud reduce IT costs related to infrastructure, freeing budget for reinvestment in other areas.
E. Applications are modernized because migration to the AWS Cloud requires companies to rearchitect and rewrite all enterprise applications.''',
     'respuesta': '''B. AWS availability and security provide the ability to improve service level agreements (SLAs) while reducing risk and unplanned downtime.
D. Companies that migrate to the AWS Cloud reduce IT costs related to infrastructure, freeing budget for reinvestment in other areas.''',
     'argumento': 'B. Migrating to the AWS Cloud provides access to the AWS global infrastructure, which offers high availability and security to businesses. AWS provides SLA´s that guarantee service availability and reduce unplanned downtime. This enhances the customer experience and reduces business risk. D. Migrating to AWS provides businesses with an opportunity to reduce IT costs related to infrastructure. With AWS, there are no upfront costs or long-term commitments, and businesses only pay for the resources they use. AWS provides an elastic infrastructure, which allows businesses to scale up or down based on demand, which helps save costs.',
     'referencia': 'https://pages.awscloud.com/global-in-gc-500-business-value-of-migration-whitepaper-learn.html?trk=9b32e983-a2c8-4455-b3a1-b385b54cba90&sc_channel=el'},
    {'pregunta': 'A company needs to identify personally identifiable information (PII), such as credit card numbers, from data that is stored in Amazon S3. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. Amazon Inspector
B. AWS Shield
C. Amazon GuardDuty
D. Amazon Macie''',
     'respuesta': 'D. Amazon Macie',
     'argumento': 'Amazon Macie discovers sensitive data using machine learning and pattern matching, provides visibility into data security risks, and enables automated protection against those risks.',
     'referencia': 'https://aws.amazon.com/macie/'},
    {'pregunta': 'Which AWS services or tools are designed to protect a workload from SQL injections, cross-site scripting, and DDoS attacks? (Choose two.)',
     'opciones': '''A. VPC endpoint
B. Virtual private gateway
C. AWS Shield Standard
D. AWS Config
E. AWS WAF''',
     'respuesta': '''C. AWS Shield Standard. 
E. AWS WAF''',
     'argumento': 'C. AWS Shield Standard: AWS Shield Standard is a built-in DDoS (Distributed Denial of Service) protection service provided by AWS. It helps protect applications against common and most frequently observed DDoS attacks. E. AWS WAF (Web Application Firewall): AWS WAF is a web application firewall that helps protect web applications from common web exploits, including SQL injections and cross-site scripting (XSS) attacks. It allows you to define customizable security rules to block or allow traffic based on various conditions and patterns.',
     'referencia': 'https://aws.amazon.com/waf/, https://aws.amazon.com/shield/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc'},
    {'pregunta': 'A company wants to forecast future costs and usage of AWS resources based on past consumption. Which AWS service or tool will provide this forecast?',
     'opciones': '''A. AWS Cost and Usage Report
B. Amazon Forecast
C. AWS Pricing Calculator
D. Cost Explorer''',
     'respuesta': 'D. Cost Explorer',
     'argumento': 'Cost Explorer: AWS Cost Explorer provides cost and usage reporting and analysis. It includes a forecasting feature that uses historical data to project future costs and usage. This allows you to estimate and plan for future spending based on your past consumption patterns.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'},
    {'pregunta': 'Which AWS services use cloud-native storage that provides replication across multiple Availability Zones by default? (Choose two.)',
     'opciones': '''A. Amazon ElastiCache
B. Amazon RDS for Oracle
C. Amazon Neptune
D. Amazon DocumentDB (with MongoDB compatibility)
E. Amazon Redshift''',
     'respuesta': '''C. Amazon Neptune. 
D. Amazon DocumentDB (with MongoDB compatibility)''',
     'argumento': 'C. Amazon Neptune: Amazon Neptune is a fully managed graph database service that provides high durability and availability by replicating data across multiple Availability Zones. It automatically handles the replication and failover of data to ensure data durability and minimize downtime. D. Amazon DocumentDB (with MongoDB compatibility): Amazon DocumentDB is a fully managed MongoDB-compatible document database service. It uses cloud-native storage that replicates data across multiple Availability Zones by default. This ensures high availability and durability of the data, with automatic failover in case of a failure.',
     'referencia': 'https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html. https://docs.aws.amazon.com/documentdb/latest/developerguide/replication.html'}, #225
    {'pregunta': 'Which AWS services are serverless? (Choose two.)',
     'opciones': '''A. AWS Fargate
B. Amazon Managed Streaming for Apache Kafka
C. Amazon EMR
D. Amazon S3
E. Amazon EC2''',
     'respuesta': '''A. AWS Fargate. 
D. Amazon S3''',
     'argumento': 'A. AWS Fargate: AWS Fargate is a serverless compute engine for containers. It allows you to run containers without managing the underlying infrastructure. You only need to define your containerized application, specify resource requirements, and AWS Fargate takes care of provisioning and managing the necessary compute resources. D. Amazon S3: Amazon S3 (Simple Storage Service) is a highly scalable and durable object storage service. It is considered serverless because you can simply store and retrieve objects without the need to provision or manage any servers. You pay for the storage and data transfer you use, without worrying about server maintenance or scaling.',
     'referencia': 'https://aws.amazon.com/serverless/'},
    {'pregunta': 'Which task is the responsibility of AWS, according to the AWS shared responsibility model?',
     'opciones': '''A. Apply guest operating system patches to Amazon EC2 instances.
B. Provide monitoring of human resources information management (HRIM) systems.
C. Perform automated backups of Amazon RDS instances.
D. Optimize the costs of running AWS services.''',
     'respuesta': 'C. Perform automated backups of Amazon RDS instances.',
     'argumento': 'AWS is responsible for managing and maintaining the underlying infrastructure and services provided by AWS, including automated backups of managed services like Amazon RDS (Relational Database Service). AWS takes care of the operational aspects of backing up the data stored in RDS instances, ensuring data durability and availability.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html'},
    {'pregunta': 'A company needs to deploy a PostgreSQL database into Amazon RDS. The database must be highly available and fault tolerant. Which AWS solution should the company use to meet these requirements?',
     'opciones': '''A. Amazon RDS with a single Availability Zone
B. Amazon RDS snapshots
C. Amazon RDS with multiple Availability Zones
D. AWS Database Migration Service (AWS DMS)''',
     'respuesta': 'C. Amazon RDS with multiple Availability Zones',
     'argumento': 'By choosing Amazon RDS with multiple Availability Zones, the company can benefit from the automatic synchronous replication of the database across multiple data centers in different Availability Zones. This setup provides redundancy and ensures that the database remains accessible even if an entire Availability Zone becomes unavailable due to a failure or outage. In such cases, Amazon RDS automatically fails over to the standby replica in another Availability Zone, minimizing downtime and ensuring high availability of the database.',
     'referencia': 'https://aws.amazon.com/rds/features/multi-az/'},
    {'pregunta': 'A company wants to add facial identification to its user verification process on an application. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. Amazon Polly
B. Amazon Transcribe
C. Amazon Lex
D. Amazon Rekognition''',
     'respuesta': 'D. Amazon Rekognition',
     'argumento': 'When you provide an image that contains a face, Amazon Rekognition detects the face in the image, analyzes the facial attributes of the face, and then returns a percent confidence score for the face and the facial attributes that are detected in the image.',
     'referencia': 'https://docs.aws.amazon.com/rekognition/latest/dg/faces.html'},
    {'pregunta': 'A company wants the ability to quickly upload its applications to the AWS Cloud without needing to provision underlying resources. Which AWS service will meet these requirements?',
     'opciones': '''A. AWS CloudFormation
B. AWS Elastic Beanstalk
C. AWS CodeDeploy
D. AWS CodeCommit''',
     'respuesta': 'B. AWS Elastic Beanstalk',
     'argumento': 'AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. With Elastic Beanstalk, you can simply upload your code and Elastic Beanstalk will automatically handle the deployment details of capacity provisioning, load balancing, and automatic scaling of your application. You can easily monitor the performance of your application and access your application logs in the Elastic Beanstalk console, or integrate Elastic Beanstalk with other AWS services to add features such as messaging and data storage.',
     'referencia': 'https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html'}, #230
    {'pregunta': 'Which AWS service monitors CPU utilization on Amazon EC2 instances?',
     'opciones': '''A. AWS CloudTrail
B. Amazon Inspector
C. AWS Config
D. Amazon CloudWatch''',
     'respuesta': 'D. Amazon CloudWatch',
     'argumento': 'You can monitor your instances using Amazon CloudWatch, which collects and processes raw data from Amazon EC2 into readable, near real-time metrics. These statistics are recorded for a period of 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html'},
    {'pregunta': 'A company needs to label its AWS resources so that the company can categorize and track costs. What should the company do to meet this requirement?',
     'opciones': '''A. Use cost allocation tags.
B. Use AWS Identity and Access Management (IAM).
C. Use AWS Organizations.
D. Use the AWS Cost Management coverage report.''',
     'respuesta': 'A. Use cost allocation tags.',
     'argumento': 'You can use tags to organize your resources, and cost allocation tags to track your AWS costs on a detailed level. After you activate cost allocation tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs.',
     'referencia': 'https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html'},
    {'pregunta': 'A company wants its employees to have access to virtual desktop infrastructure to securely access company-provided desktops through the employees personal devices. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. Amazon AppStream 2.0
B. AWS AppSync
C. Amazon FSx for Windows File Server
D. Amazon WorkSpaces''',
     'respuesta': 'D. Amazon WorkSpaces',
     'argumento': 'Amazon WorkSpaces enables you to provision virtual, cloud-based Microsoft Windows, Amazon Linux, or Ubuntu Linux desktops for your users, known as WorkSpaces. WorkSpaces eliminates the need to procure and deploy hardware or install complex software. You can quickly add or remove users as your needs change. Users can access their virtual desktops from multiple devices or web browsers.',
     'referencia': 'https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html'},
    {'pregunta': 'Which task can a company complete by using AWS Organizations?',
     'opciones': '''A. Track application deployment statuses globally.
B. Remove unused and underutilized AWS resources across all accounts.
C. Activate DDoS protection across all accounts.
D. Share pre-purchased Amazon EC2 resources across accounts.''',
     'respuesta': 'B. Remove unused and underutilized AWS resources across all accounts.',
     'argumento': 'B. Remove unused and underutilized AWS resources across all accounts: AWS Organizations is a management service that enables companies to consolidate multiple AWS accounts into an organization that can be centrally managed. It allows companies to manage policies and control access to resources across multiple accounts in a more efficient way. One of the key benefits of AWS Organizations is the ability to use it for cost optimization by removing unused and underutilized resources across all accounts.',
     'referencia': 'https://aws.amazon.com/organizations/, https://docs.aws.amazon.com/ram/latest/userguide/shareable.html'},
    {'pregunta': 'A user has been granted permission to change their own IAM user password. Which AWS services can the user use to change the password? (Choose two.)',
     'opciones': '''A. AWS Command Line Interface (AWS CLI)
B. AWS Key Management Service (AWS KMS)
C. AWS Management Console
D. AWS Resource Access Manager (AWS RAM)
E. AWS Secrets Manager''',
     'respuesta': '''A. AWS Command Line Interface (AWS CLI). 
C. AWS Management Console''',
     'argumento': 'If you have been granted permission to change your own IAM user password, you can use a special page in the AWS Management Console to do this. You can also use the AWS CLI or AWS API.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_user-change-own.html'}, #235
    {'pregunta': 'A company needs to run an application on Amazon EC2 instances. The instances cannot be interrupted at any time. The company needs an instance purchasing option that requires no long-term commitment or upfront payment. Which instance purchasing option will meet these requirements MOST cost-effectively?',
     'opciones': '''A. On-Demand Instances
B. Spot Instances
C. Dedicated Hosts
D. Reserved Instances''',
     'respuesta': 'A. On-Demand Instances',
     'argumento': 'We recommend that you use On-Demand Instances for applications with short-term, irregular workloads that cannot be interrupted.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html'},
    {'pregunta': 'A company uses Amazon EC2 instances to run its web application. The company uses On-Demand Instances and Spot Instances. The company needs to visualize its monthly spending on both types of instances. Which AWS service or feature will meet this requirement?',
     'opciones': '''A. AWS Cost Explorer
B. AWS Budgets
C. Amazon CloudWatch
D. AWS Cost Categories''',
     'respuesta': 'A. AWS Cost Explorer',
     'argumento': 'AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'},
    {'pregunta': 'Which task can a user complete by using AWS Identity and Access Management (IAM)?',
     'opciones': '''A. Validate JSON syntax from an application configuration file.
B. Analyze logs from an Amazon API Gateway call.
C. Filter traffic to or from an Amazon EC2 instance.
D. Grant permissions to applications that run on Amazon EC2 instances.''',
     'respuesta': 'D. Grant permissions to applications that run on Amazon EC2 instances.',
     'argumento': 'You can grant different permissions to different people for different resources. For example, you might allow some users complete access to Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, Amazon Redshift, and other AWS services. For other users, you can allow read-only access to just some S3 buckets, or permission to administer just some EC2 instances, or to access your billing information but nothing else.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html'},
    {'pregunta': 'A company needs to generate reports for business intelligence and operational analytics on petabytes of semistructured and structured data. These reports are produced from standard SQL queries on data that is in an Amazon S3 data lake. Which AWS service provides the ability to analyze this data?',
     'opciones': '''A. Amazon RDS
B. Amazon Neptune
C. Amazon DynamoDB
D. Amazon Redshift''',
     'respuesta': 'D. Amazon Redshift',
     'argumento': 'Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale.',
     'referencia': 'https://aws.amazon.com/redshift/'},
    {'pregunta': 'A system automatically recovers from failure when a company launches its workload on the AWS Cloud services platform. Which pillar of the AWS Well-Architected Framework does this situation demonstrate?',
     'opciones': '''A. Cost optimization
B. Operational excellence
C. Performance efficiency
D. Reliability''',
     'respuesta': 'D. Reliability',
     'argumento': 'In AWS, various services and features, such as Auto Scaling, Amazon RDS Multi-AZ, and Amazon S3 versioning, contribute to improving the reliability of workloads by automatically recovering from failures and maintaining high availability. By leveraging these AWS services, companies can design and build applications that are fault-tolerant and resilient to outages and disruptions.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.reliability.en.html'}, #240
    {'pregunta': 'Which of the following describes AWS Local Zones?',
     'opciones': '''A. A cluster of data centers in one geographic location
B. A site used by Amazon CloudFront to cache frequently accessed content
C. An extension of an AWS Region to more granular locations
D. One or more data centers with redundant power and networking''',
     'respuesta': 'C. An extension of an AWS Region to more granular locations',
     'argumento': 'AWS Local Zones allow you to use select AWS services, like compute and storage services, closer to more end-users, providing them very low latency access to the applications running locally. AWS Local Zones are also connected to the parent region via Amazon’s redundant and very high bandwidth private network, giving applications running in AWS Local Zones fast, secure, and seamless access to the rest of AWS services.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/localzones/faqs/'},
    {'pregunta': 'A retail company is migrating its IT infrastructure applications from on premises to the AWS Cloud. Which costs will the company eliminate with this migration? (Choose two.)',
     'opciones': '''A. Cost of data center operations
B. Cost of application licensing
C. Cost of marketing campaigns
D. Cost of physical server hardware
E. Cost of network management''',
     'respuesta': '''A. Cost of data center operations. 
D. Cost of physical server hardware''',
     'argumento': 'A. Cost of data center operations: Running and maintaining an on-premises data center can be expensive due to various factors like power, cooling, space, and personnel required to manage the data center facility. With AWS Cloud, the company can use the shared infrastructure and pay-as-you-go pricing model, which eliminates the need to operate and maintain a data center. D. Cost of physical server hardware: On-premises IT infrastructure requires purchasing and maintaining physical server hardware. With AWS Cloud, the company can use virtualized instances provided by AWS, and the underlying hardware is managed by AWS. This reduces the need for upfront hardware purchases and maintenance costs.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'What is a benefit of moving to the AWS Cloud in terms of improving time to market?',
     'opciones': '''A. Decreased deployment speed
B. Increased application security
C. Increased business agility
D. Increased backup capabilities''',
     'respuesta': 'C. Increased business agility',
     'argumento': 'Moving to the AWS Cloud can significantly improve time to market for companies. AWS provides a wide range of services and features that enable businesses to rapidly deploy and scale applications, reducing the time it takes to bring new products and services to market. With AWS, companies can quickly provision resources, automate processes, and leverage managed services, allowing them to focus more on innovation and less on infrastructure management.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which of the following are characteristics of a serverless application that runs in the AWS Cloud? (Choose two.)',
     'opciones': '''A. Users must manually configure Amazon EC2 instances.
B. Users have a choice of operating systems.
C. The application has built-in fault tolerance.
D. Users can run Amazon EC2 Spot Instances.
E. The application can scale based on demand.''',
     'respuesta': '''C. The application has built-in fault tolerance. 
E. The application can scale based on demand.''',
     'argumento': 'C. The application has built-in fault tolerance: AWS takes care of managing the underlying infrastructure and provides built-in fault tolerance. For example, services like AWS Lambda and Amazon DynamoDB automatically replicate data and handle failures without the need for users to manage these aspects. E. The application can scale based on demand: Serverless applications can automatically scale based on the incoming workload. Services like AWS Lambda and Amazon API Gateway automatically handle scaling to accommodate varying traffic patterns without any manual intervention.',
     'referencia': 'https://aws.amazon.com/serverless/#:~:text=Serverless%20on%20AWS&text=AWS%20offers%20technologies%20for%20running,increase%20agility%20and%20optimize%20costs'},
    {'pregunta': 'A company has existing software licenses that it wants to bring to AWS, but the licensing model requires licensing physical cores. How can the company meet this requirement in the AWS Cloud?',
     'opciones': '''A. Launch an Amazon EC2 instance with default tenancy.
B. Launch an Amazon EC2 instance on a Dedicated Host.
C. Create an On-Demand Capacity Reservation.
D. Purchase Dedicated Reserved Instances.''',
     'respuesta': 'B. Launch an Amazon EC2 instance on a Dedicated Host.',
     'argumento': 'Amazon EC2 Dedicated Hosts allow you to use your eligible software licenses from vendors such as Microsoft and Oracle on Amazon EC2, so that you get the flexibility and cost effectiveness of using your own licenses, but with the resiliency, simplicity and elasticity of AWS. An Amazon EC2 Dedicated Host is a physical server fully dedicated for your use, so you can help address corporate compliance requirements.',
     'referencia': 'https://aws.amazon.com/ec2/dedicated-hosts/'}, #245
    {'pregunta': 'A company has a complex AWS architecture. The company needs assistance from a dedicated technical professional who can suggest strategies regarding incidents, trade-offs, support, and risk management. Which AWS Support plan will provide the required support?',
     'opciones': '''A. AWS Business Support
B. AWS Enterprise Support
C. AWS Developer Support
D. AWS Basic Support''',
     'respuesta': 'B. AWS Enterprise Support',
     'argumento': '1. a complex AWS architecture. 2. needs assistance from a dedicated technical professional who can suggest strategies regarding incidents, trade-offs, support, and risk management.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/'},
    {'pregunta': 'Which of the following is an advantage that the AWS Cloud provides to users?',
     'opciones': '''A. Users eliminate the need to guess about infrastructure capacity requirements.
B. Users decrease their variable costs by maintaining sole ownership of IT hardware.
C. Users maintain control of underlying IT infrastructure hardware.
D. Users maintain control of operating systems for managed services.''',
     'respuesta': 'A. Users eliminate the need to guess about infrastructure capacity requirements.',
     'argumento': 'Stop guessing capacity – Eliminate guessing on your infrastructure capacity needs. When you make a capacity decision prior to deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes’ notice.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which AWS services can use AWS WAF to protect against common web exploitations? (Choose two.)',
     'opciones': '''A. Amazon Route 53
B. Amazon CloudFront
C. AWS Transfer Family
D. AWS Site-to-Site VPN
E. Amazon API Gateway''',
     'respuesta': '''B. Amazon CloudFront. 
E. Amazon API Gateway''',
     'argumento': 'AWS WAF can be deployed on Amazon CloudFront, the Application Load Balancer (ALB), Amazon API Gateway, and AWS AppSync. As part of Amazon CloudFront it can be part of your Content Distribution Network (CDN) protecting your resources and content at the Edge locations. As part of the Application Load Balancer it can protect your origin web servers running behind the ALBs. As part of Amazon API Gateway, it can help secure and protect your REST APIs. As part of AWS AppSync, it can help secure and protect your GraphQL APIs.',
     'referencia': 'https://aws.amazon.com/waf/faqs/#:~:text=What%20services%20does%20AWS%20WAF,content%20at%20the%20Edge%20locations.'},
    {'pregunta': 'Which controls are shared under the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Awareness and training
B. Patching of Amazon RDS
C. Configuration management
D. Physical and environmental controls
E. Service and communications protection or security''',
     'respuesta': '''A. Awareness and training. 
C. Configuration management''',
     'argumento': 'Shared Controls – Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include: Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications. Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications. Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/?nc1=h_ls'},
    {'pregunta': 'A company manages global applications that require static IP addresses. Which AWS service would enable the company to improve the availability and performance of its applications?',
     'opciones': '''A. Amazon CloudFront
B. AWS Global Accelerator
C. Amazon S3 Transfer Acceleration
D. Amazon API Gateway''',
     'respuesta': 'B. AWS Global Accelerator',
     'argumento': 'AWS Global Accelerator is a service that improves the availability and performance of applications by utilizing the AWS global network to direct traffic to the optimal AWS endpoint based on the client´s location and health of the endpoints. It provides static IP addresses that act as Anycast IP addresses, ensuring that clients are always directed to the nearest healthy endpoint. This helps to reduce latency, improve application availability, and enhance the global performance of the applications.',
     'referencia': 'https://aws.amazon.com/global-accelerator/faqs/#:~:text=A%3A%20AWS%20Global%20Accelerator%20provides,AWS%20Regions%2C%20to%20improve%20redundancy'}, #250
    {'pregunta': 'Which of the following are AWS compute services? (Choose two.)',
     'opciones': '''A. Amazon Lightsail
B. AWS Systems Manager
C. AWS CloudFormation
D. AWS Batch
E. Amazon Inspector''',
     'respuesta': '''A. Amazon Lightsail. 
D. AWS Batch''',
     'argumento': 'A. Amazon Lightsail is a simplified compute service that offers virtual private servers (VPS) with pre-configured operating systems and applications. It is designed for easy setup and is suitable for small to medium workloads. D. AWS Batch is a fully-managed service that enables developers, scientists, and engineers to easily and efficiently run batch computing workloads of any scale on AWS. It dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html'},
    {'pregunta': 'A company needs to report on events that involve the specific AWS services that the company uses. Which AWS service or resource can the company use with Amazon CloudWatch to meet this requirement?',
     'opciones': '''A. Amazon Inspector
B. AWS Personal Health Dashboard
C. AWS Trusted Advisor
D. AWS CloudTrail logs''',
     'respuesta': 'D. AWS CloudTrail logs',
     'argumento': 'AWS CloudTrail logs provide a record of all the AWS Management Console sign-in events and API calls made in the AWS account. CloudTrail logs can be used to report on events that involve specific AWS services that a company uses. The company can use CloudTrail logs with Amazon CloudWatch to monitor and alert on specific activities that occur within their AWS environment.',
     'referencia': 'https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-examples.html'},
    {'pregunta': 'A company with AWS Enterprise Support needs help understanding its monthly AWS bill and wants to implement billing best practices. Which AWS tool or resource is available to accomplish these goals?',
     'opciones': '''A. Resource tagging
B. AWS Concierge Support team
C. AWS Abuse team
D. AWS Support''',
     'respuesta': 'B. AWS Concierge Support team',
     'argumento': 'AWS Concierge Support is a benefit that comes with AWS Enterprise Support. It offers personalized, white-glove assistance to help enterprise customers with their billing inquiries, cost optimization, and other AWS-related questions and best practices. The AWS Concierge Support team provides proactive assistance, helping customers understand their monthly AWS bill and offering guidance on billing best practices to optimize costs.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/enterprise/'},
    {'pregunta': 'Which of the following is an AWS key-value database offering consistent single-digit millisecond performance at any scale?',
     'opciones': '''A. Amazon RDS
B. Amazon Aurora
C. Amazon DynamoDB
D. Amazon Redshift''',
     'respuesta': 'C. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is a fully managed, highly scalable key-value database service that delivers consistent single-digit millisecond performance at any scale. It allows you to store and retrieve any amount of data, and serves any level of request traffic. DynamoDB automatically spreads the data and traffic for a table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance. Amazon RDS, Amazon Aurora, and Amazon Redshift are also AWS services but they are not key-value database services, they are relational database services, a postgres-compatible relational database service, and a data warehousing service respectively.',
     'referencia': 'https://aws.amazon.com/dynamodb/'},
    {'pregunta': 'A company is developing a new Node.js application. The application must have a scalable NoSQL database to meet increasing demand as the popularity of the application grows. Which AWS service will meet the requirements for the database?',
     'opciones': '''A. Amazon Aurora Serverless
B. Amazon ElastiCache
C. Amazon DynamoDB
D. Amazon Redshift''',
     'respuesta': 'C. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is a fully managed NoSQL database service provided by AWS. It is designed to be highly scalable and can automatically adjust its capacity to handle the changing demand of applications. DynamoDB provides consistent single-digit millisecond latency at any scale, making it well-suited for applications that require low-latency access to data even with increasing popularity and demand. Additionally, DynamoDB automatically replicates data across multiple Availability Zones to ensure high availability and durability.',
     'referencia': 'https://aws.amazon.com/dynamodb/'}, #255
    {'pregunta': 'A company wants to set up an entire development and continuous delivery toolchain for coding, building, testing, and deploying code. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon CodeGuru
B. AWS CodeStar
C. AWS CodeCommit
D. AWS CodeDeploy''',
     'respuesta': 'B. AWS CodeStar',
     'argumento': 'AWS CodeStar is a fully managed service that enables you to quickly develop, build, and deploy applications on AWS. It provides a pre-configured continuous delivery toolchain with integrations for various AWS services like AWS CodeCommit for source code repositories, AWS CodeBuild for building code, AWS CodePipeline for continuous delivery, and AWS CodeDeploy for automated deployments. With AWS CodeStar, you can set up an entire development and continuous delivery toolchain for coding, building, testing, and deploying code with ease.',
     'referencia': 'https://docs.aws.amazon.com/codestar/latest/userguide/welcome.html'},
    {'pregunta': 'Which service enables customers to audit API calls in their AWS accounts?',
     'opciones': '''A. AWS CloudTrail
B. AWS Trusted Advisor
C. Amazon Inspector
D. AWS X-Ray''',
     'respuesta': 'A. AWS CloudTrail',
     'argumento': 'You can use CloudTrail to audit API calls made by services that are integrated with ACM. For more information about using CloudTrail, see the AWS CloudTrail User Guide. The following examples show the types of logs that can be generated depending on the AWS resources on which you provision the ACM certificate.',
     'referencia': 'https://docs.aws.amazon.com/acm/latest/userguide/ct-related.html'},
    {'pregunta': 'A company is moving its office and must establish an encrypted connection to AWS. Which AWS service will help meet this requirement?',
     'opciones': '''A. AWS VPN
B. Amazon Route 53
C. Amazon API Gateway
D. Amazon Connect''',
     'respuesta': 'A. AWS VPN',
     'argumento': 'AWS Client VPN uses the secure TLS VPN tunnel protocol to encrypt the traffic. A single VPN tunnel terminates at each Client VPN endpoint and provides users access to all AWS and on-premises resources.',
     'referencia': 'https://aws.amazon.com/vpn/features/'},
    {'pregunta': 'A company needs steady and predictable performance from its Amazon EC2 instances at the lowest possible cost. The company also needs the ability to scale resources to ensure that it has the right resources available at the right time. Which AWS service or resource will meet these requirements?',
     'opciones': '''A. Amazon CloudWatch
B. Application Load Balancer
C. AWS Batch
D. Amazon EC2 Auto Scaling''',
     'respuesta': 'D. Amazon EC2 Auto Scaling',
     'argumento': 'Amazon EC2 Auto Scaling is a service that allows you to automatically adjust the number of Amazon EC2 instances in your fleet based on demand. It helps you maintain steady and predictable performance by automatically scaling the number of instances up or down based on configured policies. When there is increased demand, EC2 Auto Scaling can add more instances, and when demand decreases, it can remove instances to optimize costs. This way, you can ensure you have the right resources available at the right time without incurring unnecessary expenses. EC2 Auto Scaling is a powerful tool for optimizing performance and cost in dynamic and variable workloads.',
     'referencia': 'https://aws.amazon.com/autoscaling/'},
    {'pregunta': 'Which action will provide documentation to help a company evaluate whether its use of the AWS Cloud is compliant with local regulatory standards?',
     'opciones': '''A. Running Amazon GuardDuty
B. Using AWS Artifact
C. Creating an AWS Support ticket
D. Evaluating AWS CloudTrail logs''',
     'respuesta': 'B. Using AWS Artifact',
     'argumento': 'AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to security and compliance reports from AWS and ISVs who sell their products on AWS Marketplace.',
     'referencia': 'https://aws.amazon.com/artifact/'}, #260
    {'pregunta': 'A company wants a cost-effective option when running its applications in an Amazon EC2 instance for short time periods. The applications can be interrupted. Which EC2 instance type will meet these requirements?',
     'opciones': '''A. Spot Instances
B. On-Demand Instances
C. Reserved Instances
D. Dedicated Instances''',
     'respuesta': 'A. Spot Instances',
     'argumento': 'Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html'},
    {'pregunta': 'A retail company is building a new mobile app. The company is evaluating whether to build the app at an on-premises data center or in the AWS Cloud. Which of the following are benefits of building this app in the AWS Cloud? (Choose two.)',
     'opciones': '''A. A large, upfront capital expense and low variable expenses
B. Increased speed for trying out new projects
C. Complete control over the physical security of the infrastructure
D. Flexibility to scale up in minutes as the application becomes popular
E. Ability to pick the specific data centers that will host the application servers''',
     'respuesta': '''B. Increased speed for trying out new projects. 
D. Flexibility to scale up in minutes as the application becomes popular''',
     'argumento': 'B. Increased speed for trying out new projects: In the AWS Cloud, you can quickly provision the necessary resources and start working on new projects without the need to procure physical hardware or wait for setup time, enabling faster experimentation and development. D. Flexibility to scale up in minutes as the application becomes popular: AWS offers the ability to scale up or down resources based on demand, allowing you to easily handle increases in user traffic or demand for your application without the need to worry about hardware limitations or capacity planning. This scalability helps ensure a smooth experience for users even during peak times.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'A developer is working on enhancing applications at AWS. The developer needs a service that can securely host GitHub-based code, repositories, and version controls. Which AWS service should the developer use?',
     'opciones': '''A. AWS CodeStar
B. Amazon CodeGuru
C. AWS CodeCommit
D. AWS CodePipeline''',
     'respuesta': 'C. AWS CodeCommit',
     'argumento': 'AWS CodeCommit is a secure, highly scalable, fully managed source control service that hosts private Git repositories.',
     'referencia': 'https://aws.amazon.com/codecommit/'},
    {'pregunta': 'What is an AWS Region?',
     'opciones': '''A. A broad set of global, cloud-based products that include compute, storage, and databases
B. A physical location around the world where data centers are clustered
C. One or more discrete data centers with redundant power, networking, and connectivity
D. A service that developers use to build applications that deliver latencies of single-digit milliseconds to users''',
     'respuesta': 'B. A physical location around the world where data centers are clustered',
     'argumento': 'An AWS (Amazon Web Services) Region is a physical location around the world where data centers are clustered. AWS operates in multiple geographic regions around the world, each of which comprises multiple Availability Zones. Each region is completely independent and designed to be isolated from the others. This means that each region is entirely self-contained, with its own infrastructure, security, and availability zones. By using multiple regions, customers can choose the location that best meets their needs in terms of latency, compliance, and other factors.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?nc1=h_ls'},
    {'pregunta': 'Which AWS benefit enables users to deploy cloud infrastructure that consists of multiple geographic regions connected by a network with low latency, high throughput, and redundancy?',
     'opciones': '''A. Economies of scale
B. Security
C. Elasticity
D. Global reach''',
     'respuesta': 'D. Global reach',
     'argumento': 'Global reach is an AWS benefit that allows users to deploy cloud infrastructure across multiple geographic regions connected by a network with low latency, high throughput, and redundancy. AWS has a vast global network of data centers and edge locations that enable users to deploy resources closer to end-users and customers, reducing latency and improving the performance of applications and services worldwide. This global infrastructure also provides redundancy and high availability, ensuring that users can access their resources and services even in the event of failures or outages in a specific region.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html'}, #265
    {'pregunta': 'A company is considering a migration from on premises to the AWS Cloud. The company´s IT team needs to offload support of the workload. What should the IT team do to accomplish this goal?',
     'opciones': '''A. Use AWS Managed Services to provision, run, and support the company infrastructure.
B. Build hardware refreshes into the operational calendar to ensure availability.
C. Use Amazon Elastic Container Service (Amazon ECS) on Amazon EC2 instances.
D. Overprovision compute capacity for seasonal events and traffic spikes to prevent downtime.''',
     'respuesta': 'A. Use AWS Managed Services to provision, run, and support the company infrastructure.',
     'argumento': 'The IT team should use AWS Managed Services to provision, run, and support the company infrastructure. AWS Managed Services provide fully managed, highly available, and scalable infrastructure services. These services are designed to offload the operational responsibilities of provisioning, running, and scaling the infrastructure. This will allow the IT team to focus on higher-value tasks such as application development, while AWS takes care of the underlying infrastructure. Managed services can include Amazon RDS, Amazon Elasticsearch Service, Amazon DynamoDB, Amazon SNS and many others.',
     'referencia': 'https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html'},
    {'pregunta': 'What is a benefit of using AWS serverless computing?',
     'opciones': '''A. Application deployment and management are not required.
B. Application security will be fully managed by AWS.
C. Monitoring and logging are not needed.
D. Management of infrastructure is offloaded to AWS.''',
     'respuesta': 'D. Management of infrastructure is offloaded to AWS.',
     'argumento': 'One of the primary benefits of using AWS serverless computing is that the management of infrastructure is offloaded to AWS. This means that the customer does not need to worry about provisioning or managing servers or other infrastructure resources. Instead, the focus can be on building and deploying applications. AWS manages the underlying infrastructure, including servers, storage, and networking, and provides automatic scaling and availability.',
     'referencia': 'https://aws.amazon.com/serverless/'},
    {'pregunta': 'A company plans to launch an application that will run in multiple locations within the United States. The company needs to identify the two AWS Regions where the application can operate at the lowest price. Which AWS service or feature should the company use to determine the Regions that offer the lowest price?',
     'opciones': '''A. Cost Explorer
B. AWS Budgets
C. AWS Trusted Advisor
D. AWS Pricing Calculator''',
     'respuesta': 'D. AWS Pricing Calculator',
     'argumento': 'The AWS Pricing Calculator is the AWS service or feature that allows the company to estimate the cost of running resources, services, and applications in different AWS Regions. By using the AWS Pricing Calculator, the company can input the required resources and configurations for their application and then compare the costs of running it in different AWS Regions. This will help the company identify the Regions that offer the lowest price for their specific application requirements.',
     'referencia': 'https://calculator.aws/#/'},
    {'pregunta': 'Which approach will enhance a user´s security on AWS?',
     'opciones': '''A. Use Multi-AZ deployments with Amazon RDS.
B. Create a hybrid architecture by using AWS Direct Connect.
C. Monitor application-specific information with AWS X-Ray.
D. Encrypt data by using AWS Key Management Service (AWS KMS).''',
     'respuesta': 'D. Encrypt data by using AWS Key Management Service (AWS KMS).',
     'argumento': 'Using AWS Key Management Service (AWS KMS) to encrypt data enhances a user´s security on AWS. AWS KMS is a managed service that allows users to create and control encryption keys used to encrypt their data stored in AWS services or applications. By encrypting data, even if there is unauthorized access to the data, it remains protected and unreadable without the appropriate encryption key. This adds an extra layer of security to sensitive data and ensures data confidentiality and integrity.',
     'referencia': 'https://aws.amazon.com/kms/features/'},
    {'pregunta': 'Which AWS service or tool is associated with an Amazon EC2 instance and acts as a virtual firewall to control inbound and outbound traffic?',
     'opciones': '''A. AWS WAF
B. AWS Shield
C. Network access control list (ACL)
D. Security group''',
     'respuesta': 'D. Security group',
     'argumento': 'A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don´t specify a security group, Amazon EC2 uses the default security group for the VPC. You can add rules to each security group that allow traffic to or from its associated instances.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html'}, #270
    {'pregunta': 'A company wants to migrate its on-premises Microsoft SQL Server database server to the AWS Cloud. The company has decided to use Amazon EC2 instances to run this database. Which of the following is the company responsible for managing, according to the AWS shared responsibility model?',
     'opciones': '''A. EC2 hypervisor
B. Security patching of the guest operating system
C. Network connectivity of the host server
D. Uptime service level agreement (SLA) for the EC2 instances''',
     'respuesta': 'B. Security patching of the guest operating system',
     'argumento': 'According to the AWS shared responsibility model, the company is responsible for tasks related to the guest operating system, which includes security patching, software updates, and other configurations within the operating system running on Amazon EC2 instances. AWS is responsible for the underlying infrastructure, such as the EC2 hypervisor and the physical network connectivity of the host server. Uptime service level agreement (SLA) for EC2 instances is also managed by AWS.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'A developer wants to deploy an application on a container-based service. The service must automatically provision and manage the backend instances. The service must provision only the necessary resources. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon EC2
B. Amazon Lightsail
C. Amazon Elastic Kubernetes Service (Amazon EKS)
D. AWS Fargate''',
     'respuesta': 'D. AWS Fargate',
     'argumento': 'AWS Fargate is a serverless, pay-as-you-go compute engine that lets you focus on building applications without managing servers. AWS Fargate is compatible with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS).',
     'referencia': 'https://aws.amazon.com/fargate/'},
    {'pregunta': 'Which tasks require use of the AWS account root user? (Choose two.)',
     'opciones': '''A. Changing an AWS Support plan
B. Modifying an Amazon EC2 instance type
C. Grouping resources in AWS Systems Manager
D. Running applications in Amazon Elastic Kubernetes Service (Amazon EKS)
E. Closing an AWS account''',
     'respuesta': '''A. Changing an AWS Support plan. 
E. Closing an AWS account''',
     'argumento': 'A. Changing an AWS Support plan: The AWS account root user has the permissions to change the AWS Support plan that is associated with the account. This can be done by logging in to the AWS Management Console, navigating to the Support Center, and selecting the appropriate plan. E. Closing an AWS account: The AWS account root user has the permissions to close an AWS account. This is a permanent action and cannot be undone, it will delete all resources associated with the account, including all data and configurations. Before closing the account, the root user should ensure that all resources are backed up and that any necessary permissions or access keys have been revoked. This can be done via AWS Management Console, AWS Support page.',
     'referencia': 'https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html'},
    {'pregunta': 'Which AWS service enables the decoupling and scaling of applications?',
     'opciones': '''A. Amazon Simple Queue Service (Amazon SQS)
B. AWS Outposts
C. Amazon S3
D. Amazon Simple Email Service (Amazon SES)''',
     'respuesta': 'A. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon SQS provides a simple and reliable way for customers to decouple and connect components (microservices) together using queues.',
     'referencia': 'https://aws.amazon.com/sqs/#:~:text=Amazon%20SQS%20provides%20a%20simple%20and%20reliable%20way%20for%20customers%20to%20decouple%20and%20connect%20components%20(microservices)%20together%20using%20queues.'},
    {'pregunta': 'Which of the following describes some of the core functionality of Amazon S3?',
     'opciones': '''A. Amazon S3 is a high-performance block storage service that is designed for use with Amazon EC2.
B. Amazon S3 is an object storage service that provides high-level performance, security, scalability, and data availability.
C. Amazon S3 is a fully managed, highly reliable, and scalable file storage system that is accessible over the industry-standard SMB protocol.
D. Amazon S3 is a scalable, fully managed elastic NFS for use with AWS Cloud services and on-premises resources.''',
     'respuesta': 'B. Amazon S3 is an object storage service that provides high-level performance, security, scalability, and data availability.',
     'argumento': 'Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can store and protect any amount of data for virtually any use case, such as data lakes, cloud-native applications, and mobile apps. With cost-effective storage classes and easy-to-use management features, you can optimize costs, organize data, and configure fine-tuned access controls to meet specific business, organizational, and compliance requirements.',
     'referencia': 'https://aws.amazon.com/s3/#:~:text=Amazon%20Simple%20Storage,and%20compliance%20requirements.'}, #275
    {'pregunta': 'How does consolidated billing help reduce costs for a company that has multiple AWS accounts?',
     'opciones': '''A. It aggregates usage across accounts so that the company can reach volume discount thresholds sooner.
B. It offers an additional 5% discount on purchases of All Upfront Reserved Instances.
C. It provides a simplified billing invoice that the company can process more quickly than a standard invoice.
D. It gives AWS resellers the ability to bill their customers for usage.''',
     'respuesta': 'A. It aggregates usage across accounts so that the company can reach volume discount thresholds sooner.',
     'argumento': 'Consolidated Billing enables you to see a combined view of AWS costs incurred by all accounts in your department or company, as well as obtain a detailed cost report for each individual AWS account associated with your paying account. Consolidated Billing may also lower your overall costs since the rolled up usage across all of your accounts could help you reach lower-priced volume tiers more quickly.',
     'referencia': 'https://aws.amazon.com/about-aws/whats-new/2010/02/09/announcing-consolidated-billing-for-aws-accounts/#:~:text=Consolidated%20Billing%20enables,tiers%20more%20quickly.'},
    {'pregunta': 'A company wants to secure its consumer web application by using SSL/TLS to encrypt traffic. Which AWS service can the company use to meet this goal?',
     'opciones': '''A. AWS WAF
B. AWS Shield
C. Amazon VPC
D. AWS Certificate Manager (ACM)''',
     'respuesta': 'D. AWS Certificate Manager (ACM)',
     'argumento': 'Use AWS Certificate Manager (ACM) to provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services and your internal connected resources. ACM removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.',
     'referencia': 'https://aws.amazon.com/certificate-manager/#:~:text=Use%20AWS%20Certificate%20Manager%20(ACM)%20to%20provision%2C%20manage%2C%20and%20deploy%20public%20and%20private%20SSL/TLS%20certificates%20for%20use%20with%20AWS%20services%20and%20your%20internal%20connected%20resources.%20ACM%20removes%20the%20time%2Dconsuming%20manual%20process%20of%20purchasing%2C%20uploading%2C%20and%20renewing%20SSL/TLS%20certificates.'},
    {'pregunta': 'Which of the following are advantages of moving to the AWS Cloud? (Choose two.)',
     'opciones': '''A. Users can implement all AWS services in seconds.
B. AWS assumes all responsibility for the security of infrastructure and applications.
C. Users experience increased speed and agility.
D. Users benefit from massive economies of scale.
E. Users can move hardware from their data center to the AWS Cloud.''',
     'respuesta': '''C. Users experience increased speed and agility. 
D. Users benefit from massive economies of scale.''',
     'argumento': 'Moving to the AWS Cloud provides increased speed and agility as users can provision and scale resources quickly, enabling faster application deployment and reducing time-to-market. AWS operates at a large scale, which allows them to provide cost-effective solutions. This enables users to benefit from significant cost savings compared to running infrastructure on-premises.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'A company stores configuration files in an Amazon S3 bucket. These configuration files must be accessed by applications that are running on Amazon EC2 instances. According to AWS security best practices, how should the company grant permissions to allow the applications for access the S3 bucket?',
     'opciones': '''A. Use the AWS account root user access keys.
B. Use the AWS access key ID and the EC2 secret access key.
C. Use an IAM role with the necessary permissions.
D. Activate multi-factor authentication (MFA) and versioning on the S3 bucket.''',
     'respuesta': 'C. Use an IAM role with the necessary permissions.',
     'argumento': 'AWS security best practices recommend using IAM roles to grant permissions to AWS resources, including S3 buckets. By attaching an IAM role to the EC2 instances, applications running on those instances can securely access the S3 bucket without needing to use access keys or credentials directly. This approach provides a more secure and manageable way to grant access to AWS resources from EC2 instances.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html'},
    {'pregunta': 'A company needs an AWS service that will continuously monitor the company´s AWS account for suspicious activity. The service must have the ability to initiate automated actions against threats that are identified in the security findings. Which service will meet these requirements?',
     'opciones': '''A. AWS Trusted Advisor
B. Amazon Detective
C. Amazon Inspector
D. Amazon GuardDuty''',
     'respuesta': 'D. Amazon GuardDut',
     'argumento': 'Amazon GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and delivers detailed security findings for visibility and remediation.',
     'referencia': 'https://aws.amazon.com/guardduty/'}, #280
    {'pregunta': 'A company wants to analyze streaming user data and respond to customer queries in real time. Which AWS service can meet these requirements?',
     'opciones': '''A. Amazon QuickSight
B. Amazon Redshift
C. Amazon Kinesis Data Analytics
D. AWS Data Pipeline''',
     'respuesta': 'C. Amazon Kinesis Data Analytics',
     'argumento': '\With Amazon Kinesis Data Streams, you can build custom applications that process or analyze streaming data for specialized needs. You can add various types of data such as clickstreams, application logs, and social media to a Kinesis data stream from hundreds of thousands of sources. Within seconds, the data will be available for your applications to read and process from the stream.',
     'referencia': 'https://aws.amazon.com/kinesis/data-streams/faqs/?nc=sn&loc=6&refid=fc81dabe-57e1-4c46-8d33-cfd3acf1ef08'},
    {'pregunta': 'Who can create and manage access keys for an AWS account root user?',
     'opciones': '''A. The AWS account owner
B. An IAM user that has administrator permissions
C. IAM users within a designated group
D. An IAM user that has the required role''',
     'respuesta': 'A. The AWS account owner',
     'argumento': 'Only the AWS account root user has the permissions to create and manage access keys for the AWS account. IAM users, even those with administrative permissions, cannot manage access keys for the root user. It is recommended to avoid using the root user for day-to-day tasks and instead create IAM users with appropriate permissions to manage resources and access keys. This follows the principle of least privilege and enhances the security of the AWS account.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html'},
    {'pregunta': 'Which AWS service can help a company detect an outage of its website servers and redirect users to alternate servers?',
     'opciones': '''A. Amazon CloudFront
B. Amazon GuardDuty
C. Amazon Route 53
D. AWS Trusted Advisor''',
     'respuesta': 'C. Amazon Route 53',
     'argumento': 'Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. It can be used to detect an outage of a company´s website servers and redirect users to alternate servers through the use of health checks and failover routing policies. It can also be used to route users to the optimal location for faster content delivery using geographic routing.',
     'referencia': 'https://aws.amazon.com/about-aws/whats-new/2013/02/11/announcing-dns-failover-for-route-53/'},
    {'pregunta': 'A web application is hosted on AWS using an Elastic Load Balancer, multiple Amazon EC2 instances, and Amazon RDS. Which security measures fall under the responsibility of AWS? (Choose two.)',
     'opciones': '''A. Running a virus scan on EC2 instances
B. Protecting against IP spoofing and packet sniffing
C. Installing the latest security patches on the RDS instance
D. Encrypting communication between the EC2 instances and the Elastic Load Balancer
E. Configuring a security group and a network access control list (NACL) for EC2 instances''',
     'respuesta': '''B. Protecting against IP spoofing and packet sniffing 
C. Installing the latest security patches on the RDS instance''',
     'argumento': 'Periodically, Amazon RDS performs maintenance on Amazon RDS resources. Maintenance most often involves updates to the DB instance´s underlying hardware, underlying operating system (OS), or database engine version. Updates to the operating system most often occur for security issues and should be done as soon as possible. Some maintenance items require that Amazon RDS take your DB instance offline for a short time. Maintenance items that require a resource to be offline include required operating system or database patching. Required patching is automatically scheduled only for patches that are related to security and instance reliability. Such patching occurs infrequently (typically once every few months) and seldom requires more than a fraction of your maintenance window.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html'},
    {'pregunta': 'Which of the following is an AWS Well-Architected Framework design principle for operational excellence in the AWS Cloud?',
     'opciones': '''A. Go global in minutes.
B. Make frequent, small, reversible changes.
C. Implement a strong foundation of identity and access management.
D. Stop spending money on hardware infrastructure for data center operations.''',
     'respuesta': 'B. Make frequent, small, reversible changes.',
     'argumento': 'Make frequent, small, reversible changes: Design workloads to allow components to be updated regularly. Make changes in small increments that can be reversed if they fail (without affecting customers when possible).',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.operationalExcellence.en.html'}, #285
    {'pregunta': 'Which AWS service provides intelligent recommendations to improve code quality and identify an application´s most expensive lines of code?',
     'opciones': '''A. Amazon CodeGuru
B. AWS CodeStar
C. AWS CodeCommit
D. AWS CodeDeploy''',
     'respuesta': 'A. Amazon CodeGuru',
     'argumento': 'CodeGuru has two components: Amazon CodeGuru Security and Amazon CodeGuru Profiler. CodeGuru Security is a machine learning (ML) and program analysis-based tool that finds security vulnerabilities in your Java, Python, and JavaScript code. CodeGuru Security also scans for hardcoded credentials. CodeGuru Profiler optimizes performance for applications running in production and identifies the most expensive lines of code, reducing operational costs significantly.',
     'referencia': 'https://aws.amazon.com/codeguru/faqs/'},
    {'pregunta': 'A company wants to expand from one AWS Region into a second AWS Region. What does the company need to do to expand into the second Region?',
     'opciones': '''A. Contact an AWS account manager to sign a new contract.
B. Move an Availability Zone to the second Region.
C. Begin to deploy resources in the second Region.
D. Download the AWS Management Console for the second Region.''',
     'respuesta': 'C. Begin to deploy resources in the second Region.',
     'argumento': 'To expand into a second AWS Region, the company needs to start deploying resources in that Region. AWS Regions are separate geographic locations where AWS services are hosted. Each Region is isolated from other Regions and consists of multiple Availability Zones. By deploying resources in a second Region, the company can achieve high availability and disaster recovery capabilities, as well as bring its applications closer to end-users in different geographic areas.',
     'referencia': 'https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-region.html'},
    {'pregunta': 'Which AWS service provides storage that can be mounted across multiple Amazon EC2 instances?',
     'opciones': '''A. Amazon WorkSpaces
B. Amazon Elastic File System (Amazon EFS)
C. AWS Database Migration Service (AWS DMS)
D. AWS Snowball Edge''',
     'respuesta': 'B. Amazon Elastic File System (Amazon EFS)',
     'argumento': 'Amazon Elastic File System (Amazon EFS) is a scalable, fully managed, and cloud-native file storage service provided by AWS. It provides a simple and scalable file system that can be mounted across multiple Amazon EC2 instances. This means that multiple EC2 instances within the same VPC can share the same file system, enabling them to access and modify files concurrently. Amazon EFS is suitable for use cases that require shared file storage across multiple instances, such as content management systems, web hosting, and development environments.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html'},
    {'pregunta': 'A company needs to deploy applications in the AWS Cloud as quickly as possible. The company also needs to minimize the complexity that is related to the management of AWS resources. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS Config
B. AWS Elastic Beanstalk
C. Amazon EC2
D. Amazon Personalize''',
     'respuesta': 'B. AWS Elastic Beanstalk',
     'argumento': 'AWS Elastic Beanstalk makes it even easier for developers to quickly deploy and manage applications in the AWS Cloud. Developers simply upload their application, and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring.',
     'referencia': 'https://aws.amazon.com/elasticbeanstalk/faqs/'},
    {'pregunta': 'A company has a set of databases that are stored on premises. The company wants to bring its existing Microsoft SQL Server licenses when the company moves the databases to run on Amazon EC2 instances. Which EC2 instance purchasing option should the company use to meet these requirements?',
     'opciones': '''A. Dedicated Instances
B. Reserved Instances
C. Dedicated Hosts
D. Spot Instances''',
     'respuesta': 'C. Dedicated Hosts',
     'argumento': 'Dedicated Hosts are physical servers with EC2 instance capacity that are dedicated to a specific AWS account. When using Dedicated Hosts, you have full control over the host, including the ability to bring your existing server-bound software licenses, such as Microsoft SQL Server, and run them on these dedicated instances. By using Dedicated Hosts, you can leverage your existing Microsoft SQL Server licenses and maintain compliance with licensing requirements while running your databases on EC2 instances in the AWS Cloud.',
     'referencia': 'https://aws.amazon.com/windows/resources/licensing/'}, #290
    {'pregunta': 'Which of the following is a way to use Amazon EC2 Auto Scaling groups to scale capacity in the AWS Cloud?',
     'opciones': '''A. Scale the number of EC2 instances in or out automatically, based on demand.
B. Use serverless EC2 instances.
C. Scale the size of EC2 instances up or down automatically, based on demand.
D. Transfer unused CPU resources between EC2 instances.''',
     'respuesta': 'A. Scale the number of EC2 instances in or out automatically, based on demand.',
     'argumento': 'Amazon EC2 Auto Scaling groups allows you to automatically scale the number of Amazon Elastic Compute Cloud (EC2) instances in your application in or out, in response to changes in demand for your application. This helps ensure that you have the correct number of instances running to handle the traffic to your application. Auto Scaling can be configured to use CloudWatch alarms to determine when to scale the number of instances, and it can also be configured to scale based on a schedule. This can be done by creating policies that increase or decrease the number of instances, based on CloudWatch metrics, schedule or even by using a custom metric.',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html'},
    {'pregunta': 'A company discovered unauthorized access to resources in its on-premises data center. Upon investigation, the company found that the requests originated from a resource hosted on AWS. Which AWS team should the company contact to report this issue?',
     'opciones': '''A. AWS Customer Service team
B. AWS Sales team
C. AWS Abuse team
D. AWS Technical Support team''',
     'respuesta': 'C. AWS Abuse team',
     'argumento': 'If a company discovers unauthorized access or abuse originating from a resource hosted on AWS, they should contact the AWS Abuse team. The Abuse team handles reports of inappropriate behavior, security incidents, and other potential violations of AWS Acceptable Use Policy (AUP). They will investigate the issue and take appropriate actions to address the situation.',
     'referencia': 'https://aws.amazon.com/premiumsupport/knowledge-center/report-aws-abuse/'},
    {'pregunta': 'Which of the following are aspects of the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Configuration management of infrastructure devices is the customer's responsibility.
B. For Amazon S3, AWS operates the infrastructure layer, the operating systems, and the platforms.
C. AWS is responsible for protecting the physical cloud infrastructure.
D. AWS is responsible for training the customer's employees on AWS products and services.
E. For Amazon EC2, AWS is responsible for maintaining the guest operating system.''',
     'respuesta': '''B. For Amazon S3, AWS operates the infrastructure layer, the operating systems, and the platforms. 
C. AWS is responsible for protecting the physical cloud infrastructure.''',
     'argumento': 'In the AWS shared responsibility model, the responsibility for security and management is shared between AWS and the customer. AWS takes care of the underlying infrastructure, operating systems, and platforms for services like Amazon S3. However, customers are responsible for using these services securely, setting up access controls, and managing their own data. Additionally, AWS is responsible for physical security and protection of the cloud infrastructure, while customers are responsible for configuring and managing their applications and data.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/#:~:text=AWS%20responsibility%20%E2%80%9CSecurity%20of%20the,that%20run%20AWS%20Cloud%20services'},
    {'pregunta': 'A company needs real-time guidance to follow AWS best practices to save money, improve system performance, and close security gaps. Which AWS service should the company use?',
     'opciones': '''A. Amazon GuardDuty
B. AWS Trusted Advisor
C. AWS Management Console
D. AWS Systems Manager''',
     'respuesta': 'B. AWS Trusted Advisor',
     'argumento': 'AWS Trusted Advisor is a service that provides real-time guidance to help customers follow AWS best practices. It offers recommendations in areas such as cost optimization, performance improvements, security enhancements, and fault tolerance. Trusted Advisor continuously monitors your AWS environment and provides actionable insights to save money, improve system performance, and close security gaps based on AWS best practices.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/'},
    {'pregunta': 'A company wants to organize its users so that the company can grant permissions to the users as a group. Which AWS service or tool can the company use to meet this requirement?',
     'opciones': '''A. Security groups
B. AWS Identity and Access Management (IAM)
C. Resource groups
D. AWS Security Hub''',
     'respuesta': 'B. AWS Identity and Access Management (IAM)',
     'argumento': 'AWS Identity and Access Management (IAM) is a service that enables the company to control and manage access to AWS resources. IAM allows the company to create and manage users, groups and roles, and to grant permissions to those groups and roles. This enables the company to grant permissions to a group of users, rather than having to grant permissions individually to each user. With IAM, the company can create IAM users and groups and then grant permissions to those groups using policies. This allows the company to grant permissions to a set of users as a group, which helps to simplify the process of managing access to resources.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html'}, #295
    {'pregunta': 'A company runs applications that process credit card information. Auditors have asked if the AWS environment has changed since the previous audit. If the AWS environment has changed, the auditors want to know how it has changed. Which AWS services can provide this information? (Choose two.)',
     'opciones': '''A. AWS Artifact
B. AWS Trusted Advisor
C. AWS Config
D. AWS CloudTrail
E. AWS Identity and Access Management (IAM)''',
     'respuesta': '''C. AWS Config. 
D. AWS CloudTrail''',
     'argumento': 'AWS Config is a service that provides a detailed inventory of AWS resources and configuration changes to these resources. It can be used to track changes to resources over time, including changes to configurations, relationships between resources, and compliance with internal policies or external regulations. AWS CloudTrail is a service that records all API calls made in an AWS account and stores the information in an Amazon S3 bucket. This information can be used for security analysis, resource change tracking, and compliance auditing.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/30/'},
    {'pregunta': 'A company wants to use a template to reliably provision, manage, and update its infrastructure in the AWS Cloud. Which AWS service will meet these requirements?',
     'opciones': '''A. AWS Lambda
B. AWS CloudFormation
C. AWS Fargate
D. AWS CodeDeploy''',
     'respuesta': 'B. AWS CloudFormation',
     'argumento': 'AWS CloudFormation is a service that allows you to create and manage a collection of related AWS resources using templates. It enables you to provision and update resources in a safe, predictable, and repeatable way. With CloudFormation, you define your infrastructure as code in a template, which can be version-controlled and shared. The template describes all the resources and their configurations, and CloudFormation takes care of creating and managing those resources as specified in the template. Using AWS CloudFormation, you can launch complex infrastructures with a single click, update existing stacks, and rollback to previous versions if needed. It helps you maintain consistency, reduce human errors, and automate the process of managing AWS resources, making it a reliable way to provision, manage, and update your infrastructure in the AWS Cloud.',
     'referencia': 'https://aws.amazon.com/cloudformation/resources/templates/'},
    {'pregunta': 'A company is reviewing the current costs of running its own infrastructure on premises. The company wants to compare these on-premises costs to the costs of running infrastructure in the AWS Cloud. How should the company make this comparison?',
     'opciones': '''A. Review the AWS shared responsibility model.
B. Audit existing software and hardware licensing costs.
C. Analyze the AWS Well-Architected Framework.
D. Use Migration Evaluator.''',
     'respuesta': 'D. Use Migration Evaluator.',
     'argumento': 'Migration Evaluator provides a comprehensive cost analysis, including infrastructure costs, licensing costs, and other associated expenses. It takes into account various factors like resource utilization, storage requirements, and data transfer costs to generate an accurate comparison between on-premises costs and the costs of running infrastructure in the AWS Cloud.',
     'referencia': 'https://aws.amazon.com/migration-evaluator/'},
    {'pregunta': 'A company needs a low-code, visual workflow service that developers can use to build distributed applications. Which AWS service is designed to meet these requirements?',
     'opciones': '''A. AWS Step Functions
B. AWS Config
C. AWS Lambda
D. Amazon CloudWatch''',
     'respuesta': 'A. AWS Step Functions',
     'argumento': 'AWS Step Functions is a low-code, visual workflow service provided by AWS. It allows developers to build and coordinate applications using visual workflows. With Step Functions, you can design and build distributed applications easily, defining the steps and conditions for the workflow visually through a graphical interface. Step Functions supports a wide range of AWS services, and it can be used to create complex workflows that involve multiple AWS resources and microservices. It simplifies the process of creating distributed applications and makes it easier to manage the flow of tasks and actions.',
     'referencia': 'https://aws.amazon.com/step-functions/'},
    {'pregunta': 'A company wants to accelerate migration from its data center to the AWS Cloud. Which combination of AWS services should the company use to meet this requirement? (Choose two.)',
     'opciones': '''A. Amazon Connect
B. AWS Direct Connect
C. AWS Server Migration Service (AWS SMS)
D. Amazon Route 53
E. AWS Organizations''',
     'respuesta': '''B. AWS Direct Connect. 
C. AWS Server Migration Service (AWS SMS)''',
     'argumento': 'AWS Direct Connect is a networking service that provides an alternative to using the internet to connect to AWS. Using AWS Direct Connect, data that would have previously been transported over the internet is delivered through a private network connection between your facilities and AWS. In many circumstances, private network connections can reduce costs, increase bandwidth, and provide a more consistent network experience than internet-based connections. All AWS services, including Amazon Elastic Compute Cloud (EC2), Amazon Virtual Private Cloud (VPC), Amazon Simple Storage Service (S3), and Amazon DynamoDB can be used with AWS Direct Connect.',
     'referencia': 'https://aws.amazon.com/directconnect/faqs/?nc=sn&loc=6'}, #300
    {'pregunta': 'What should a user do if the user loses an IAM secret access key?',
     'opciones': '''A. Retrieve the secret access key by using the IAM console.
B. Create a new user with a new access key and a new secret access key.
C. Rotate the secret access key.
D. Request a new secret access key from AWS Support.''',
     'respuesta': 'B. Create a new user with a new access key and a new secret access key.',
     'argumento': 'Rotating access keys is a proactive security measure where you generate new keys to replace the existing ones to enhance security. Creating a new user with new access keys is a common approach when an IAM secret access key is lost. By creating a new user, you can start with a clean slate and have full control over the new access keys and permissions associated with the user.',
     'referencia': 'https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/'},
    {'pregunta': 'A company wants to deploy a Docker application to the AWS Cloud. However, the company does not want to manage the underlying servers. Which combination of AWS services should the company use to meet these requirements? (Choose two.)',
     'opciones': '''A. Amazon EC2
B. Amazon EC2 Auto Scaling
C. AWS Elastic Beanstalk
D. Amazon CloudFront
E. AWS Fargate''',
     'respuesta': '''C. AWS Elastic Beanstalk. 
E. AWS Fargate''',
     'argumento': '"AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). AWS Fargate makes it easy to focus on building your applications. Fargate eliminates the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design."',
     'referencia': 'https://aws.amazon.com/fargate/faqs/?nc=sn&loc=4'},
    {'pregunta': 'A company needs to transfer 60 TB of data to the AWS Cloud in a secure manner. Which of the following should the company use to meet these requirements?',
     'opciones': '''A. AWS Snowball Edge device
B. Amazon Elastic Block Store (Amazon EBS)
C. Amazon Elastic File System (Amazon EFS)
D. Amazon S3''',
     'respuesta': 'A. AWS Snowball Edge device',
     'argumento': '"AWS Snowball is a service that provides secure, rugged devices, so you can bring AWS computing and storage capabilities to your edge environments, and transfer data into and out of AWS. Those rugged devices are commonly referred to as AWS Snowball or AWS Snowball Edge devices. Previously, AWS Snowball referred specifically to an early hardware version of these devices, however that model has been replaced by updated hardware. Now the AWS Snowball service operates with Snowball Edge devices, which include on-board computing capabilities as well as storage."',
     'referencia': 'https://aws.amazon.com/snowball/faqs/'},
    {'pregunta': 'A gaming company wants to move its on-premises environment to AWS. The company needs its resources to be highly available. Which benefit does the AWS Cloud provide to meet this requirement?',
     'opciones': '''A. Reliability
B. The AWS shared responsibility model
C. Security
D. Agility''',
     'respuesta': 'A. Reliability',
     'argumento': 'In any system of reasonable complexity, it is expected that failures will occur. Reliability requires that your workload be aware of failures as they occur and take action to avoid impact on availability. Workloads must be able to both withstand failures and automatically repair issues.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.pillar.reliability.en.html'},
    {'pregunta': 'An ecommerce company has been monitoring usage of its online store that is hosted on a fleet of Amazon EC2 instances. Surges in traffic occur every weekend day at the same time and last for approximately 4 hours. Which AWS service should the company use to ensure that there are enough instances to meet the surges in demand?',
     'opciones': '''A. AWS Lambda
B. Amazon EventBridge (Amazon CloudWatch Events)
C. Elastic Load Balancing (ELB)
D. Amazon EC2 Auto Scaling''',
     'respuesta': 'D. Amazon EC2 Auto Scaling',
     'argumento': 'Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove EC2 instances using scaling policies that you define. Dynamic or predictive scaling policies let you add or remove EC2 instance capacity to service established or real-time demand patterns. The fleet management features of Amazon EC2 Auto Scaling help maintain the health and availability of your fleet.',
     'referencia': 'https://aws.amazon.com/ec2/autoscaling/'}, #305
    {'pregunta': 'A company needs stateless network filtering for its VPC. Which AWS service, tool, or feature will meet this requirement?',
     'opciones': '''A. AWS PrivateLink
B. Security group
C. Network access control list (ACL)
D. AWS WAF''',
     'respuesta': 'C. Network access control list (ACL)',
     'argumento': 'AWS Network Access Control Lists (ACLs) are used to provide stateless filtering for the inbound and outbound traffic of a VPC subnet. They act as a virtual firewall for controlling traffic at the subnet level. ACLs evaluate rules in a specific order, and each rule is stateless, meaning that it doesn´t track the state of the traffic like a stateful firewall would.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/31/'},
    {'pregunta': 'A company needs to audit its AWS resources. The company must document any changes that have been made to the resources. Which AWS service will meet these requirements?',
     'opciones': '''A. AWS Artifact
B. AWS Config
C. Amazon Inspector
D. Amazon CloudWatch''',
     'respuesta': 'B. AWS Config',
     'argumento': 'AWS Config continually assesses, audits, and evaluates the configurations and relationships of your resources on AWS, on premises, and on other clouds.',
     'referencia': 'https://aws.amazon.com/config/'},
    {'pregunta': 'A company needs fully managed, highly reliable, and scalable file storage that is accessible over the Server Message Block (SMB) protocol. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon S3
B. Amazon Elastic File System (Amazon EFS)
C. Amazon FSx for Windows File Server
D. Amazon Elastic Block Store (Amazon EBS)''',
     'respuesta': 'C. Amazon FSx for Windows File Server',
     'argumento': 'Amazon FSx for Windows File Server provides fully managed, highly reliable, and scalable file storage that is accessible over the industry-standard Service Message Block (SMB) protocol. It is built on Windows Server, delivering a wide range of administrative features such as user quotas, end-user file restore, and Microsoft Active Directory (AD) integration.',
     'referencia': 'https://aws.amazon.com/fsx/windows/faqs/'},
    {'pregunta': 'Which AWS service should a company use to create a NoSQL database?',
     'opciones': '''A. Amazon Aurora
B. Amazon DynamoDB
C. Amazon Redshift
D. Amazon Neptune''',
     'respuesta': 'B. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don´t have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.',
     'referencia': 'https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html'},
    {'pregunta': 'A company is migrating to the AWS Cloud. The company requires consultative review and guidance for its applications during the migration. After the migration is complete, the company requires a response within 30 minutes if business-critical systems go down. Which AWS Support plans meet these requirements? (Choose two.)',
     'opciones': '''A. AWS Enterprise Support
B. AWS Enterprise On-Ramp Support
C. AWS Developer Support
D. AWS Basic Support
E. AWS Business Support''',
     'respuesta': '''A. AWS Enterprise Support. 
B. AWS Enterprise On-Ramp Support''',
     'argumento': 'AWS Enterprise Support and AWS Enterprise On-Ramp Support are both premium support plans that offer 24/7 support with a response time of 30 minutes for business-critical incidents. They also offer consultative review and guidance for applications, which is what the company requires during the migration.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/'}, #310
    {'pregunta': 'A company needs an AWS Support plan that provides programmatic case management through the AWS Support API. Which support plan will meet this requirement MOST cost-effectively?',
     'opciones': '''A. AWS Business Support
B. AWS Basic Support
C. AWS Developer Support
D. AWS Enterprise Support''',
     'respuesta': 'A. AWS Business Support',
     'argumento': 'AWS Developer Support" does not have programmatic case management. Business support is the next tier that has (most cost effective)',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/'},
    {'pregunta': 'A company that operates in the AWS Cloud wants to test workloads and team responses to simulated events. The company will conduct an exercise to identify potential issues that need to be addressed. Which design principle of the AWS Well-Architected Framework does this exercise represent?',
     'opciones': '''A. Anticipate failure.
B. Automatically recover from failure.
C. Measure overall cost efficiency.
D. Implement loosely coupled dependencies.''',
     'respuesta': 'A. Anticipate failure',
     'argumento': 'Anticipate failure: Perform “pre-mortem” exercises to identify potential sources of failure so that they can be removed or mitigated. Test your failure scenarios and validate your understanding of their impact. Test your response procedures to verify that they are effective, and that teams are familiar with their process. Set up regular game days to test workloads and team responses to simulated events.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html'},
    {'pregunta': 'Which AWS services provide high availability across multiple Availability Zones by default? (Choose two.)',
     'opciones': '''A. Amazon EC2
B. Amazon Elastic Block Store (Amazon EBS)
C. Amazon Elastic File System (Amazon EFS)
D. Amazon Redshift
E. Amazon S3''',
     'respuesta': '''C. Amazon Elastic File System (Amazon EFS). 
E. Amazon S3''',
     'argumento': 'Amazon Elastic File System (Amazon EFS) and Amazon S3 are both designed to provide high availability and durability by default. Amazon EFS automatically stores data across multiple Availability Zones within a region to provide high availability and durability, while Amazon S3 stores data across multiple facilities and multiple devices within those facilities to provide high availability and durability.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/32/'},
    {'pregunta': 'A company needs to perform queries and interactively search and analyze log data. Which AWS service or feature will meet this requirement?',
     'opciones': '''A. Amazon EventBridge (Amazon CloudWatch Events)
B. Amazon CloudWatch anomaly detection
C. Amazon CloudWatch Logs Insights
D. Amazon CloudWatch Logs streams''',
     'respuesta': 'C. Amazon CloudWatch Logs Insights',
     'argumento': 'CloudWatch Logs Insights enables you to interactively search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you more efficiently and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.',
     'referencia': 'https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html'},
    {'pregunta': 'A company has an on-premises Oracle database. The company spends a significant amount of time on database administration activities. The company is moving the database to AWS and needs to minimize the time that is required for those administration activities. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. Amazon ElastiCache
B. Amazon EC2
C. Amazon RDS
D. Amazon DynamoDB''',
     'respuesta': 'C. Amazon RDS',
     'argumento': 'Amazon RDS for Oracle is a fully managed commercial database that makes it easy to set up, operate, and scale Oracle deployments in the cloud. Amazon RDS frees you up to focus on innovation and application development by managing time-consuming database administration tasks, including provisioning, backups, software patching, monitoring, and hardware scaling. You can run Amazon RDS for Oracle under two different licensing models – “License Included” and “Bring-Your-Own-License (BYOL)”. In the "License Included" service model, you do not need separately purchased Oracle licenses; the Oracle Database software has been licensed by AWS.',
     'referencia': 'https://aws.amazon.com/rds/oracle/'}, #315
    {'pregunta': 'A company is running an Amazon EC2 instance in a VPC. Which of the following can the company use to route and filter incoming network requests for the EC2 instance?',
     'opciones': '''A. Route tables and web application firewalls
B. Security groups and route tables
C. Security groups and a network intrusion system
D. Route tables and AWS Shield''',
     'respuesta': 'B. Security groups and route tables',
     'argumento': 'Security groups control inbound and outbound traffic to an Amazon EC2 instance, acting as virtual firewalls. Route tables, on the other hand, determine the traffic´s path between subnets within a Virtual Private Cloud (VPC) or to a virtual private gateway for accessing resources outside the VPC.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/32/'},
    {'pregunta': 'A company plans to migrate its custom marketing application and order-processing application to AWS. The company needs to deploy the applications on different types of instances with various configurations of CPU, memory, storage, and networking capacity. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS Lambda
B. Amazon Cognito
C. Amazon Athena
D. Amazon EC2''',
     'respuesta': 'D. Amazon EC2',
     'argumento': 'Amazon Elastic Compute Cloud (Amazon EC2) offers the broadest and deepest compute platform, with over 600 instances and choice of the latest processor, storage, networking, operating system, and purchase model to help you best match the needs of your workload. We are the first major cloud provider that supports Intel, AMD, and Arm processors, the only cloud with on-demand EC2 Mac instances, and the only cloud with 400 Gbps Ethernet networking. We offer the best price performance for machine learning training, as well as the lowest cost per inference instances in the cloud. More SAP, high performance computing (HPC), ML, and Windows workloads run on AWS than any other cloud.',
     'referencia': 'https://aws.amazon.com/ec2/'},
    {'pregunta': 'A company wants to set up a Domain Name System (DNS) record for its application with a failover routing policy that is based on health checks. Which AWS service or resource should the company use to achieve this goal?',
     'opciones': '''A. Amazon Connect
B. Application Load Balancer
C. Amazon Route 53
D. AWS WAF''',
     'respuesta': 'C. Amazon Route 53',
     'argumento': 'Amazon Route 53 provides highly available and scalable Domain Name System (DNS), domain name registration, and health-checking web services. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like example.com into the numeric IP addresses, such as 192.0.2.1, that computers use to connect to each other. You can combine your DNS with health-checking services to route traffic to healthy endpoints or to independently monitor and/or alarm on endpoints.',
     'referencia': 'https://aws.amazon.com/route53/faqs/'},
    {'pregunta': 'Which of the following are AWS best practice recommendations for the use of AWS Identity and Access Management (IAM)? (Choose two.)',
     'opciones': '''A. Use the AWS account root user tor daily access.
B. Use access keys and secret access keys on Amazon EC2.
C. Rotate credentials on a regular basis.
D. Create a shared set of access keys for system administrators.
E. Configure multi-factor authentication (MFA).''',
     'respuesta': '''C. Rotate credentials on a regular basis. 
E. Configure multi-factor authentication (MFA).''',
     'argumento': 'C. Rotate credentials on a regular basis: AWS recommends rotating credentials (access keys, passwords, and access tokens) every 90 days. This helps to ensure that even if a set of credentials is compromised, an attacker will only have access for a limited period of time. E. Configure multi-factor authentication (MFA): Enabling multi-factor authentication (MFA) for privileged users and roles can help to protect against unauthorized access, even if a user´s password or access keys are compromised.',
     'referencia': 'https://aws.amazon.com/es/iam/resources/best-practices/'},
    {'pregunta': 'A company needs to store code in a version control system. The company also needs to continually deploy updated code through a series of automated steps (build, test, package, and deploy). Which combination of AWS services will meet these requirements? (Choose two.)',
     'opciones': '''A. AWS CloudFormation
B. AWS CodeCommit
C. AWS Control Tower
D. AWS Elastic Beanstalk
E. AWS CodePipoline''',
     'respuesta': '''B. AWS CodeCommit. 
E. AWS CodePipoline''',
     'argumento': 'With AWS CodePipeline, you model the full release process for building your code, deploying to pre-production environments, testing your application and releasing it to production. AWS CodePipeline then builds, tests, and deploys your application according to the defined workflow every time there is a code change',
     'referencia': 'https://aws.amazon.com/codepipeline/faqs/?nc=sn&loc=5, https://aws.amazon.com/codecommit, https://aws.amazon.com/codepipeline'}, #320
    {'pregunta': 'An ecommerce company has deployed a new web application on Amazon EC2 instances. The company wants to distribute incoming HTTP traffic evenly across all running instances. Which AWS service or resource will meet this requirement?',
     'opciones': '''A. Amazon EC2 Auto Scaling
B. Application Load Balancer
C. Gateway Load Balancer
D. Network Load Balancer''',
     'respuesta': 'B. Application Load Balancer',
     'argumento': 'Routes and load balances at the application layer (HTTP/HTTPS), and supports path-based routing. An Application Load Balancer can route requests to ports on one or more registered targets, such as EC2 instances, in your virtual private cloud (VPC).',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html'},
    {'pregunta': 'Which of the following are advantages of moving from on premises to the AWS Cloud? (Choose two.)',
     'opciones': '''A. Trade variable expenses for capital expenses.
B. Eliminate costs related to running and maintaining data centers.
C. Benefit from massive economies of scale.
D. Eliminate the need to tram IT staff.
E. Gam the ability to reserve capacity for 7 years or more.''',
     'respuesta': '''B. Eliminate costs related to running and maintaining data centers. 
C. Benefit from massive economies of scale.''',
     'argumento': 'B. Moving to the AWS Cloud can eliminate the costs associated with running and maintaining on-premises data centers, such as hardware procurement, maintenance, cooling, power, and facility costs. C. AWS operates at a massive scale, which allows them to achieve economies of scale that can lead to cost savings for customers. This is especially beneficial for businesses since they can leverage AWS´s existing infrastructure and resources to achieve cost efficiency.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'A company is using an Amazon RDS database to run reports that are input/output (I/O) intensive. Which AWS service can be used to improve the database performance?',
     'opciones': '''A. Amazon DynamoDB Accelerator (DAX)
B. Amazon EMR
C. Amazon ElastiCache
D. Amazon Redshift''',
     'respuesta': 'C. Amazon ElastiCache',
     'argumento': 'Amazon ElastiCache improves the performance of web applications by allowing you to retrieve information from a fast, managed, in-memory system, instead of relying entirely on slower disk-based databases.',
     'referencia': 'https://aws.amazon.com/elasticache/faqs/'},
    {'pregunta': 'Which AWS service provides automated backups of data by default?',
     'opciones': '''A. Amazon S3
B. Amazon Aurora
C. Amazon ElastiCache for Memcached
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'B. Amazon Aurora',
     'argumento': 'Amazon Aurora provides automated backups of data by default. When you create an Aurora DB cluster, the service automatically creates one or more automated backups of the DB cluster, known as a "backup window". These backups are stored in Amazon S3 and are retained according to your specified retention period.',
     'referencia': 'https://aws.amazon.com/rds/aurora/'},
    {'pregunta': 'Which AWS service is a fully hosted version control service?',
     'opciones': '''A. AWS CodeCommit
B. AWS CodeBuild
C. AWS CodeDeploy
D. AWS CodeStar''',
     'respuesta': 'A. AWS CodeCommit',
     'argumento': 'AWS CodeCommit is a version control service hosted by Amazon Web Services that you can use to privately store and manage assets (such as documents, source code, and binary files) in the cloud.',
     'referencia': 'https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html'}, #325
    {'pregunta': 'A company is using Amazon RDS. Which task is the company´s responsibility, according to the AWS shared responsibility model?',
     'opciones': '''A. Apply encryption options for the database.
B. Manage the underlying server hardware on which Amazon RDS runs.
C. Apply patches to the underlying operating system.
D. Apply minor patches to the database.''',
     'respuesta': 'A. Apply encryption options for the database.',
     'argumento': 'According to the AWS shared responsibility model, AWS is responsible for the security of the cloud infrastructure, while customers are responsible for the security in the cloud, which includes securing their applications, data, and operating systems. Applying encryption options for the database is the responsibility of the company, as it is related to securing the data. The other options are the responsibility of AWS.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html'},
    {'pregunta': 'A company recently created its first AWS account. Which AWS services will require the use of a VPC? (Choose two.)',
     'opciones': '''A. Amazon S3
B. Amazon Elastic File System (Amazon EFS)
C. Amazon Cognito
D. Amazon DynamoDB
E. Amazon EC2''',
     'respuesta': '''B. Amazon Elastic File System (Amazon EFS). 
E. Amazon EC2''',
     'argumento': 'E. Amazon EC2 - Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. Instances of EC2 are launched in a VPC. B. Amazon Elastic File System (Amazon EFS) - Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system that can be used with AWS Cloud services and on-premises resources. Amazon EFS is a regional service that supports VPCs.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/33/'},
    {'pregunta': 'A user has an AWS account with a Business-level AWS Support plan and needs assistance with handling a production service disruption. Which action should the user take?',
     'opciones': '''A. Contact the dedicated AWS technical account manager (TAM).
B. Contact the dedicated AWS Concierge Support team.
C. Open a business-critical system down support case.
D. Open a production system down support case.''',
     'respuesta': 'D. Open a production system down support case.',
     'argumento': 'Business-level AWS Support plan can open is "Production system down"',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/'},
    {'pregunta': 'A company is using Amazon EC2 instances. Which tasks are the company´s responsibility, according to the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Maintain the network infrastructure.
B. Patch the guest operating system.
C. Configure a security group on deployed EC2 instances.
D. Provide physical security for the underlying hardware of the EC2 instances.
E. Manage the underlying hypervisor.''',
     'respuesta': '''B. Patch the guest operating system. 
C. Configure a security group on deployed EC2 instances.''',
     'argumento': 'Patching the guest operating system is the responsibility of the customer. AWS is responsible for patching and maintaining the underlying infrastructure. Configuring a security group on deployed EC2 instances is the customer´s responsibility. AWS is responsible for providing the security of the infrastructure and the underlying hypervisor.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/33/'},
    {'pregunta': 'Which of the following does Amazon CloudFront use to distribute content to users around the world?',
     'opciones': '''A. Amazon VPC
B. AWS Local Zones
C. Edge locations
D. Availability Zones''',
     'respuesta': 'C. Edge locations',
     'argumento': 'Amazon CloudFront is a web service that gives businesses and web application developers an easy and cost effective way to distribute content with low latency and high data transfer speeds. Like other AWS services, Amazon CloudFront is a self-service, pay-per-use offering, requiring no long term commitments or minimum fees. With CloudFront, your files are delivered to end-users using a global network of edge locations.',
     'referencia': 'https://aws.amazon.com/cloudfront/faqs/?nc=sn&loc=5&dn=2'}, #330
    {'pregunta': 'Which pillar of the AWS Well-Architected Framework includes the continual improvement of processes and procedures as a priority?',
     'opciones': '''A. Cost optimization
B. Reliability
C. Performance efficiency
D. Operational excellence''',
     'respuesta': 'D. Operational excellence',
     'argumento': 'The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html'},
    {'pregunta': 'Which of the following consists of one or more isolated data centers in the same regional area that are interconnected through low-latency networks?',
     'opciones': '''A. Availability Zone
B. Edge location
C. AWS Region
D. Private networking''',
     'respuesta': 'A. Availability Zone',
     'argumento': 'An Availability Zone (AZ) is an isolated data center within an AWS Region that is designed to be highly available and fault-tolerant. It consists of one or more data centers in the same geographic area, interconnected through low-latency networks. Each Availability Zone is designed to be physically and logically separate from other Availability Zones within the same Region to provide resilience and redundancy.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/34/'},
    {'pregunta': 'Which AWS service or resource helps on-premises applications connect to AWS Cloud-based storage and caches the data locally for low-latency access?',
     'opciones': '''A. AWS Direct Connect
B. AWS Storage Gateway
C. Amazon S3
D. AWS Snowball Edge''',
     'respuesta': 'B. AWS Storage Gateway',
     'argumento': 'AWS Storage Gateway is a hybrid cloud storage service that enables on-premises applications to seamlessly access AWS Cloud-based storage. It provides a local cache for frequently accessed data to ensure low-latency access, while also storing data in the cloud for durability and scalability.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/34/'},
    {'pregunta': 'Which AWS service or feature enables users to get one bill and easily track charges for multiple AWS accounts?',
     'opciones': '''A. AWS Organizations
B. Cost Explorer
C. AWS Trusted Advisor
D. AWS Management Console''',
     'respuesta': 'A. AWS Organizations',
     'argumento': 'AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html'},
    {'pregunta': 'A company has a global website with static content. Which AWS service will deliver the static content with low latency?',
     'opciones': '''A. AWS Lambda
B. Amazon CloudFront
C. Amazon EC2 Auto Scaling
D. AWS Compute Optimizer''',
     'respuesta': 'B. Amazon CloudFront',
     'argumento': 'The AWS service that will deliver the static content with low latency is Amazon CloudFront. It is a content delivery network (CDN) service that caches content at edge locations around the world, which helps to reduce latency by serving content from the edge location closest to the user.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/34/'}, #335
    {'pregunta': 'Which AWS service provides alerts when an AWS event may impact a company´s AWS resources?',
     'opciones': '''A. AWS Personal Health Dashboard
B. AWS Service Health Dashboard
C. AWS Trusted Advisor
D. AWS Infrastructure Event Management''',
     'respuesta': 'A. AWS Personal Health Dashboard',
     'argumento': 'While the Service Health Dashboard displays the general status of Amazon Web Services services, Personal Health Dashboard gives you a personalized view into the performance and availability of the Amazon Web Services services underlying your Amazon Web Services resources.',
     'referencia': 'https://controltower.aws-management.tools/ops/health/'},
    {'pregunta': 'A company manages an on-premises MySQL database on a Windows server. The company wants to migrate the database to AWS and needs a solution that will reduce the administrative overhead of the database. Which AWS service will meet this requirement?',
     'opciones': '''A. Amazon Redshift
B. Amazon ElastiCache
C. Amazon RDS
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'C. Amazon RDS',
     'argumento': 'Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. Choose from seven popular engines — Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server — and deploy on-premises with Amazon RDS on AWS Outposts.',
     'referencia': 'https://aws.amazon.com/rds/'},
    {'pregunta': 'Which AWS service can be used to provide an on-demand, cloud-based contact center?',
     'opciones': '''A. AWS Direct Connect
B. Amazon Connect
C. AWS Support Center
D. AWS Managed Services''',
     'respuesta': 'B. Amazon Connect',
     'argumento': 'Amazon Connect is an AWS service that provides an on-demand, cloud-based contact center that enables businesses to provide high-quality customer service at a lower cost than traditional contact center solutions. It is a fully managed service that can scale up or down to meet changing business needs, and it provides features such as automatic call distribution, call recording, and analytics.',
     'referencia': 'https://aws.amazon.com/connect/'},
    {'pregunta': 'Which benefit of cloud computing gives a company the ability to deploy applications to users all over the world through a network of AWS Regions, Availability Zones, and edge locations?',
     'opciones': '''A. Economy of scale
B. Global reach
C. Agility
D. High availability''',
     'respuesta': 'B. Global reach',
     'argumento': 'One of the benefits of cloud computing is global reach, which allows a company to deploy applications to users all over the world through a network of AWS regions, availability zones, and edge locations. This enables companies to reach a global customer base and respond to market demands quickly and cost-effectively. Economy of scale refers to the ability to achieve lower costs per unit through increased production and efficiency. Agility refers to the ability to respond to changing business needs quickly and easily. High availability refers to the ability to ensure that an application or service is always available, even in the event of a failure or outage.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/34/'},
    {'pregunta': 'Which AWS service is a relational database compatible with MySQL and PostgreSQL?',
     'opciones': '''A. Amazon Redshift
B. Amazon DynamoDB
C. Amazon Aurora
D. Amazon Neptune''',
     'respuesta': 'C. Amazon Aurora',
     'argumento': 'Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL and PostgreSQL compatibility. Aurora gives you the performance and availability of commercial-grade databases at one-tenth the cost.',
     'referencia': 'https://aws.amazon.com/rds/aurora/'}, #340
    {'pregunta': 'A company uses a database that has a simple sign-up page to create users, and a basic login form to authenticate users so they can access the database. The company wants to give users the ability to store personal information, but user access must be controlled in a more secure and reliable way. Which AWS service or feature will meet these requirements?',
     'opciones': '''A. Security groups
B. Amazon GuardDuty
C. AWS Secrets Manager
D. Amazon Cognito''',
     'respuesta': 'D. Amazon Cognito',
     'argumento': 'With Amazon Cognito, you can add user sign-up and sign-in features and control access to your web and mobile applications. Amazon Cognito provides an identity store that scales to millions of users, supports social and enterprise identity federation, and offers advanced security features to protect your consumers and business. Built on open identity standards, Amazon Cognito supports various compliance regulations and integrates with frontend and backend development resources.',
     'referencia': 'https://aws.amazon.com/cognito/'},
    {'pregunta': 'A company is running multiple workloads in the AWS Cloud and recently began investigating ways to reduce costs. The company is already running fault-tolerant workloads on Amazon EC2 that perform periodic checkpoints in case of an outage. Which AWS service or pricing model can provide the GREATEST cost savings?',
     'opciones': '''A. Capacity Reservations
B. Amazon Lightsail
C. Spot Instances
D. Dedicated Hosts''',
     'respuesta': 'C. Spot Instances',
     'argumento': 'Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity in the AWS cloud. Spot Instances are available at up to a 90% discount compared to On-Demand prices. You can use Spot Instances for various stateless, fault-tolerant, or flexible applications such as big data, containerized workloads, CI/CD, web servers, high-performance computing (HPC), and test & development workloads.',
     'referencia': 'https://aws.amazon.com/ec2/spot/'},
    {'pregunta': 'A company is undergoing a security audit. The audit includes security validation and compliance validation of the AWS infrastructure and services that the company uses. The auditor needs to locate compliance-related information and must download AWS security and compliance documents. These documents include the System and Organization Control (SOC) reports. Which AWS service or group can provide these documents?',
     'opciones': '''A. AWS Abuse team
B. AWS Artifact
C. AWS Support
D. AWS Config''',
     'respuesta': 'B. AWS Artifact',
     'argumento': 'AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to security and compliance reports from AWS and ISVs who sell their products on AWS Marketplace. You can use AWS Artifact Reports to download AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and System and Organization Control (SOC) reports.',
     'referencia': 'https://aws.amazon.com/artifact/, https://aws.amazon.com/artifact/faq/'},
    {'pregunta': 'Which of the following are design principles of the reliability pillar of the AWS Well-Architected Framework? (Choose two.)',
     'opciones': '''A. Perform operations as code.
B. Stop guessing capacity.
C. Adopt serverless architecture whenever possible.
D. Use build and deployment management systems.
E. Make changes to infrastructure by using automation.''',
     'respuesta': '''B. Stop guessing capacity. 
E. Make changes to infrastructure by using automation.''',
     'argumento': 'Stop guessing capacity: A common cause of failure in on-premises workloads is resource saturation, when the demands placed on a workload exceed the capacity of that workload (this is often the objective of denial of service attacks). In the cloud, you can monitor demand and workload utilization, and automate the addition or removal of resources to maintain the optimal level to satisfy demand without over- or under-provisioning. There are still limits, but some quotas can be controlled and others can be managed (see Manage Service Quotas and Constraints). Manage change in automation: Changes to your infrastructure should be made using automation. The changes that need to be managed include changes to the automation, which then can be tracked and reviewed.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html'},
    {'pregunta': 'A company needs to perform data processing once a week that typically takes about 5 hours to complete. Which AWS service should the company use for this workload?',
     'opciones': '''A. AWS Lambda
B. Amazon EC2
C. AWS CodeDeploy
D. AWS Wavelength''',
     'respuesta': 'B. Amazon EC2',
     'argumento': 'For a data processing workload that needs to run for a specific duration, Amazon EC2 instances would be more appropriate. EC2 instances provide virtual machines that you can configure with the necessary resources for your workload, and you can control the duration for which they run. You can choose an instance type that suits your processing needs and set up automation scripts or jobs to initiate and control the processing.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/35/'}, #345
    {'pregunta': 'A company is developing a new web application. The company must give users the ability to log in to the application through social identity providers. Which AWS service will meet these requirements?',
     'opciones': '''A. AWS Directory Service
B. Amazon Cognito
C. AWS Identity and Access Management (IAM)
D. AWS Single Sign-On''',
     'respuesta': 'B. Amazon Cognito',
     'argumento': 'Amazon Cognito is a service that provides user authentication and authorization services, including the ability to log in through social identity providers such as Google, Facebook, and Amazon. It´s commonly used for building applications with user registration, login, and account management functionality.',
     'referencia': 'https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html#feature-overview'},
    {'pregunta': 'According to the AWS shared responsibility model, which activities are the customer´s responsibility for security in the AWS Cloud? (Choose two.)',
     'opciones': '''A. Hardware maintenance
B. Amazon EC2 operating system patching
C. API access control for AWS resources
D. Configuration management of infrastructure devices
E. Maintenance of an Availability Zone''',
     'respuesta': '''B. Amazon EC2 operating system patching. 
C. API access control for AWS resources''',
     'argumento': 'Amazon EC2 operating system patching: Customers are responsible for patching the operating system of their Amazon EC2 instances. This includes tasks such as applying security updates and bug fixes. API access control for AWS resources: Customers are responsible for controlling who has access to their AWS resources. This includes tasks such as creating and managing users and groups, and assigning permissions to resources.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/35/'},
    {'pregunta': 'Which service is an AWS in-memory data store service?',
     'opciones': '''A. Amazon Aurora
B. Amazon RDS
C. Amazon DynamoDB
D. Amazon ElastiCache''',
     'respuesta': 'D. Amazon ElastiCache',
     'argumento': 'Amazon ElastiCache is a web service that makes it easy to deploy and run Memcached or Redis protocol-compliant server nodes in the cloud. Amazon ElastiCache improves the performance of web applications by allowing you to retrieve information from a fast, managed, in-memory system, instead of relying entirely on slower disk-based databases. The service simplifies and offloads the management, monitoring and operation of in-memory environments, enabling your engineering resources to focus on developing applications. Using Amazon ElastiCache, you can not only improve load and response times to user actions and queries, but also reduce the cost associated with scaling web applications.',
     'referencia': 'https://aws.amazon.com/elasticache/faqs/'},
    {'pregunta': 'Which duty is a responsibility of AWS under the AWS shared responsibility model?',
     'opciones': '''A. Identity and access management
B. Server-side encryption (SSE)
C. Firewall configuration
D. Maintaining physical hardware''',
     'respuesta': 'D. Maintaining physical hardware',
     'argumento': 'AWS responsibility “Security of the Cloud” - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'Which guidelines are key AWS architectural design principles? (Choose two.)',
     'opciones': '''A. Design for fixed resources.
B. Build scalable architectures.
C. Use tightly coupled components.
D. Use managed services when possible.
E. Design for human interaction''',
     'respuesta': '''B. Build scalable architectures. 
D. Use managed services when possible.''',
     'argumento': 'AWS Managed Services (AMS) helps you adopt AWS at scale and operate more efficiently and securely. We leverage standard AWS services and offer guidance and execution of operational best practices with specialized automations, skills, and experience that are contextual to your environment and applications. AMS provides proactive, preventative, and detective capabilities that raise the operational bar and help reduce risk without constraining agility, allowing you to focus on innovation. AMS extends your team with operational capabilities including monitoring, incident management, AWS Incident Detection and Response, security, patch, backup, and cost optimization.',
     'referencia': 'https://aws.amazon.com/managed-services/, https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.scalability.en.html'}, #350
    {'pregunta': 'A company is planning to build a workload in the AWS Cloud. The company needs to estimate the costs of the network, compute, storage, and database for the workload. Which AWS service or tool should the company use to generate this estimate?',
     'opciones': '''A. AWS Budgets
B. AWS Organizations
C. Cost Explorer
D. AWS Pricing Calculator''',
     'respuesta': 'D. AWS Pricing Calculator',
     'argumento': 'AWS Pricing Calculator is a web-based planning tool that you can use to create estimates for your AWS use cases. You can use it to model your solutions before building them, explore the AWS service price points, and review the calculations behind your estimates. You can use it to help you plan how you spend, find cost saving opportunities, and make informed decisions when using Amazon Web Services. AWS Pricing Calculator is useful for those who have never used AWS. It´s also useful for those who want to reorganize or expand their AWS usage. You don´t need any experience with the cloud or AWS to use AWS Pricing Calculator.',
     'referencia': 'https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html'},
    {'pregunta': 'A user is a new AWS account owner who has no special access requirements. What should this user do with the AWS account root user access keys?',
     'opciones': '''A. Share the keys with all relevant internal users so that those users can programmatically access AWS services.
B. Post the keys on GitHub to provide development teams with access to AWS services.
C. Use the keys for access, but do not share the keys with anyone.
D. Delete the keys and create IAM users.''',
     'respuesta': 'C. Use the keys for access, but do not share the keys with anyone.',
     'argumento': 'We strongly recommend that you do not use the root user for your everyday tasks, even the administrative ones. Instead, adhere to the best practice of using the root user only to create your first IAM user. Then securely lock away the root user credentials and use them to perform only a few account and service management tasks',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html'},
    {'pregunta': 'Which AWS service allows for file sharing between multiple Amazon EC2 instances?',
     'opciones': '''A. AWS Direct Connect
B. AWS Snowball Edge
C. AWS Backup
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'D. Amazon Elastic File System (Amazon EFS)',
     'argumento': 'Multiple compute instances, including Amazon EC2, Amazon ECS, and AWS Lambda, can access an Amazon EFS file system at the same time. Therefore, an EFS file system can provide a common data source for workloads and applications that are running on more than one compute instance or server.',
     'referencia': 'https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html'},
    {'pregunta': 'A company is running and managing its own Docker environment on Amazon EC2 instances. The company wants an alternative to help manage cluster size, scheduling, and environment maintenance. Which AWS service meets these requirements?',
     'opciones': '''A. AWS Lambda
B. Amazon RDS
C. AWS Fargate
D. Amazon Athena''',
     'respuesta': 'C. AWS Fargate',
     'argumento': 'AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Elastic Kubernetes Service (EKS). It allows users to run containers without managing the underlying EC2 instances, making it a good option for managing cluster size, scheduling, and environment maintenance. With Fargate, users only need to define their containers and the required resources, and Fargate will take care of the rest, including scaling, patching, and monitoring. Therefore, Fargate is the AWS service that best meets the company´s requirements.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/36/'},
    {'pregunta': 'Which databases are available on Amazon RDS? (Choose two.)',
     'opciones': '''A. Sybase
B. Microsoft SQL Server
C. IBM Db2
D. MongoDB
E. PostgreSQL''',
     'respuesta': '''B. Microsoft SQL Server. 
E. PostgreSQL''',
     'argumento': 'Microsoft SQL Server (Option B): Amazon RDS supports various editions of Microsoft SQL Server, including Express, Web, Standard, and Enterprise editions. This allows you to easily set up, operate, and scale a SQL Server database in the cloud. PostgreSQL (Option E): Amazon RDS also supports PostgreSQL, which is a powerful open-source relational database management system. RDS makes it easier to set up, operate, and scale PostgreSQL databases.',
     'referencia': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html'}, #355
    {'pregunta': 'Which Amazon S3 feature or storage class uses the AWS backbone network and edge locations to reduce latencies from the end user to Amazon S3?',
     'opciones': '''A. S3 Cross-Region Replication
B. S3 Transfer Acceleration
C. S3 Event Notifications
D. S3 Standard-Infrequent Access (S3 Standard-IA)''',
     'respuesta': 'B. S3 Transfer Acceleration',
     'argumento': 'S3 Transfer Acceleration improves transfer performance by routing traffic through Amazon CloudFront’s globally distributed Edge Locations and over AWS backbone networks, and by using network protocol optimizations.',
     'referencia': 'https://medium.com/awesome-cloud/aws-amazon-s3-transfer-acceleration-overview-6baa7b029c27'},
    {'pregunta': 'Which design principles of the AWS Well-Architected Framework help increase reliability? (Choose two.)',
     'opciones': '''A. Automatically recover from failure.
B. Enable traceability.
C. Scale horizontally to increase workload availability.
D. Automate security best practices.
E. Keep people away from data.''',
     'respuesta': '''A. Automatically recover from failure. 
C. Scale horizontally to increase workload availability.''',
     'argumento': 'Automatically recover from failure: This principle focuses on the ability of the workload to automatically recover from failure. It involves identifying potential points of failure and designing systems that can automatically recover from them. Scale horizontally to increase workload availability: This principle involves designing systems that can automatically scale horizontally to increase availability. By distributing the workload across multiple instances, the system can handle increased traffic and provide a more reliable experience to users.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/36/'},
    {'pregunta': 'Management at a large company wants to avoid long-term contracts and is interested in AWS to move from fixed costs to variable costs. What is the value proposition of AWS for this company?',
     'opciones': '''A. Economy of scale
B. Pay-as-you-go pricing
C. Volume discounts
D. Cost optimization''',
     'respuesta': 'B. Pay-as-you-go pricing',
     'argumento': 'AWS offers you a pay-as-you-go approach for pricing for the vast majority of our cloud services. With AWS you pay only for the individual services you need, for as long as you use them, and without requiring long-term contracts or complex licensing. AWS pricing is similar to how you pay for utilities like water and electricity. You only pay for the services you consume, and once you stop using them, there are no additional costs or termination fees.',
     'referencia': 'https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all'},
    {'pregunta': 'Which AWS service should a company use to decouple large monolithic applications into smaller microservices components?',
     'opciones': '''A. AWS Direct Connect
B. Amazon Lightsail
C. Amazon Simple Queue Service (Amazon SQS)
D. Amazon CloudWatch''',
     'respuesta': 'C. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon Simple Queue Service (SQS) is a managed message queuing service technical professionals and developers use to send, store and retrieve multiple messages of various sizes asynchronously. The service enables users to decouple individual microservices, distributed systems and serverless applications from one another and to scale them without requiring the user to establish and maintain their own message queues.',
     'referencia': 'https://www.techtarget.com/searchaws/definition/Amazon-Simple-Queue-Service-SQS'},
    {'pregunta': 'A company´s system administrator discovers that someone logged in to the company´s AWS account during the weekend and terminated an Amazon EC2 instance. Which AWS service should the system administrator use to identify who made this change?',
     'opciones': '''A. Amazon Inspector
B. Amazon Pinpoint
C. AWS CloudTrail
D. AWS Trusted Advisor''',
     'respuesta': 'C. AWS CloudTrail',
     'argumento': 'You can troubleshoot operational issues by leveraging the Amazon API call history produced by Amazon CloudTrail. For example, you can quickly identify the most recent changes made to resources in your environment, including creation, modification, and deletion of Amazon Web Services resources (e.g., Amazon EC2 instances, Amazon VPC security groups, and Amazon EBS volumes).',
     'referencia': 'https://www.amazonaws.cn/en/cloudtrail/#:~:text=Amazon%20CloudTrail%20increases%20visibility%20into,and%20when%20the%20calls%20occurred.'}, #360
    {'pregunta': 'Which AWS service or tool lists all the users in an account and reports on the status of account details, including passwords, access keys, and multi-factor authentication (MFA) devices?',
     'opciones': '''A. AWS Shield
B. AWS Trusted Advisor
C. Amazon Inspector
D. IAM credential report''',
     'respuesta': 'D. IAM credential report',
     'argumento': 'You can generate and download a credential report that lists all users in your account and the status of their various credentials, including passwords, access keys, and MFA devices. You can get a credential report from the AWS Management Console, the AWS SDKs and Command Line Tools, or the IAM API.',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html'},
    {'pregunta': 'Which AWS service offers threat detection and continuously monitors for malicious activity and unauthorized behavior in AWS accounts?',
     'opciones': '''A. Amazon Macie
B. AWS Config
C. Amazon GuardDuty
D. Amazon Inspector''',
     'respuesta': 'C. Amazon GuardDuty',
     'argumento': 'Amazon GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and delivers detailed security findings for visibility and remediation. Continuously monitor your AWS accounts, instances, serverless and container workloads, users, databases, and storage for potential threats.',
     'referencia': 'https://aws.amazon.com/guardduty/'},
    {'pregunta': 'A company needs to use Amazon S3 to store audio files that are each 5 megabytes in size. The company will rarely access the files, but the company must be able to retrieve the files immediately. Which S3 storage class will meet these requirements MOST cost-effectively?',
     'opciones': '''A. S3 Standard
B. S3 Standard-Infrequent Access (S3 Standard-IA)
C. S3 Glacier Flexible Retrieval
D. S3 Glacier Deep Archive''',
     'respuesta': 'B. S3 Standard-Infrequent Access (S3 Standard-IA)',
     'argumento': 'S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval charge. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files.',
     'referencia': 'https://aws.amazon.com/s3/storage-classes/'},
    {'pregunta': 'A user wants to control AWS services by using the AWS CLI. What are the MINIMUM security credentials that the user needs to achieve this goal?',
     'opciones': '''A. AWS account user name and password
B. Multi-factor authentication (MFA)
C. Access keys
D. Key pairs''',
     'respuesta': 'C. Access keys',
     'argumento': 'You can use access keys to sign programmatic requests to the AWS CLI or AWS API (directly or using the AWS SDK). Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access key. You must use both the access key ID and secret access key together to authenticate your requests.',
     'referencia': 'https://docs.aws.amazon.com/cli/latest/userguide/cli-security-iam.html'},
    {'pregunta': 'A company has stopped all of its Amazon EC2 instances but monthly billing charges continue to occur. What could be causing this? (Choose two.)',
     'opciones': '''A. Amazon Elastic Block Store (Amazon EBS) storage charges
B. Operating system charges
C. Hardware charges
D. Elastic IP charges
E. Input/output (I/O) charges''',
     'respuesta': '''A. Amazon Elastic Block Store (Amazon EBS) storage charges. 
D. Elastic IP charges''',
     'argumento': 'A. Amazon Elastic Block Store (Amazon EBS) storage charges D. Elastic IP charges. These two are chargeable even when the instance is not running. Once the instances are shut down, EBS & Elastic IP have to be deleted to avoid getting charged',
     'referencia': 'https://aws.amazon.com/premiumsupport/knowledge-center/ec2-billing-terminated/'}, #365
    {'pregunta': 'A company has set up its IT infrastructure in the AWS Cloud. The company wants to receive detailed reports that break down AWS costs by the hour. The reports must be placed in an Amazon S3 bucket. Which AWS tool will meet these requirements?',
     'opciones': '''A. AWS Cost and Usage Reports
B. AWS Pricing Calculator
C. Cost Explorer
D. AWS Budgets''',
     'respuesta': 'A. AWS Cost and Usage Reports',
     'argumento': 'You can receive reports that break down your costs by the hour, day, or month, by product or product resource, or by tags that you define yourself. AWS updates the report in your bucket once a day in comma-separated value (CSV) format.',
     'referencia': 'https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html'},
    {'pregunta': 'Which AWS service or feature enables users to block the incoming or outgoing traffic associated with specific IP addresses flowing through a VPC?',
     'opciones': '''A. Network ACLs
B. Security groups
C. AWS Identity and Access Management (IAM)
D. AWS WAF''',
     'respuesta': 'A. Network ACLs',
     'argumento': 'Security groups are tied to an instance whereas Network ACLs are tied to the subnet. Network ACLs are applicable at the subnet level, so any instance in the subnet with an associated NACL will follow the rules of NACL. That’s not the case with security groups, security groups have to be assigned explicitly to the instance.',
     'referencia': 'https://medium.com/awesome-cloud/aws-difference-between-security-groups-and-network-acls-adc632ea29ae#:~:text=Security%20groups%20are,to%20the%20instance'},
    {'pregunta': 'What is the customer ALWAYS responsible for managing, according to the AWS shared responsibility model?',
     'opciones': '''A. Software licenses
B. Networking
C. Customer data
D. Encryption keys''',
     'respuesta': 'C. Customer data',
     'argumento': 'Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/#:~:text=Customers%20are%20responsible%20for%20managing%20their%20data%20(including%20encryption%20options)%2C%20classifying%20their%20assets%2C%20and%20using%20IAM%20tools%20to%20apply%20the%20appropriate%20permissions.'},
    {'pregunta': 'Which Reserved Instance (RI) provides the HIGHEST average cost savings compared to an On-Demand Instance?',
     'opciones': '''A. 1-year, No Upfront, Standard RI
B. 1-year, All Upfront, Convertible RI
C. 3-year, All Upfront, Standard RI
D. 3-year, No Upfront, Convertible RI''',
     'respuesta': 'C. 3-year, All Upfront, Standard RI',
     'argumento': 'When it comes to Reserved Instances (RIs), the longer the term and the more upfront payment made, the higher the average cost savings compared to an On-Demand Instance. 3-year, All Upfront, Standard RI provides the highest average cost savings compared to an On-Demand Instance. This option allows you to commit to a 3-year term, pay for the entire term upfront and receive the highest level of savings. This option is ideal for predictable workloads that can be planned and managed for a longer period of time.',
     'referencia': 'https://aws.amazon.com/ec2/pricing/reserved-instances/pricing/'},
    {'pregunta': 'Elasticity in the AWS Cloud refers to which of the following? (Choose two.)',
     'opciones': '''A. How quickly an Amazon EC2 instance can be restarted
B. The ability to rightsize resources as demand shifts
C. The maximum amount of RAM an Amazon EC2 instance can use
D. The pay-as-you-go billing model
E. How easily resources can be procured when they are needed''',
     'respuesta': '''B. The ability to rightsize resources as demand shifts. 
E. How easily resources can be procured when they are needed''',
     'argumento': 'The ability to acquire resources as you need them and release resources when you no longer need them. In the cloud, you want to do this automatically. Most people, when thinking of cloud computing, think of the ease with which they can procure resources when needed. This is only one aspect to elasticity. The other aspect is to contract when they no longer need resources. Scale out and scale in. Scale up and scale down.',
     'referencia': 'https://wa.aws.amazon.com/wat.concept.elasticity.en.html'}, #370
    {'pregunta': 'A company has a set of ecommerce applications. The applications need to be able to send messages to each other. Which AWS service meets this requirement?',
     'opciones': '''A. AWS Auto Scaling
B. Elastic Load Balancing
C. Amazon Simple Queue Service (Amazon SQS)
D. Amazon Kinesis Data Streams''',
     'respuesta': 'C. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon Simple Queue Service (Amazon SQS) lets you send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.',
     'referencia': 'https://aws.amazon.com/sqs/'},
    {'pregunta': 'A company wants to receive alerts when resources that are launched in the company´s AWS account reach 80% of their service quotas. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. AWS CloudTrail
B. AWS Trusted Advisor
C. AWS Config
D. Amazon Inspector''',
     'respuesta': 'B. AWS Trusted Advisor',
     'argumento': 'Service quotas are the maximum number of resources that you can create in an AWS account. AWS implements quotas to provide highly available and reliable service to all customers, and protects you from unintentional spend. Trusted Advisor will notify you once you reach more than 80% of a service quota. You can then follow recommendations to delete resources or request a quota increase.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/#:~:text=AWS%20Trusted%20Advisor%20provides%20recommendations,costs%2C%20and%20monitor%20service%20quotas.'},
    {'pregunta': 'Which pillar of the AWS Well-Architected Framework is focused on the ability of a workload to perform its intended function correctly and consistently at the expected time?',
     'opciones': '''A. Performance efficiency
B. Operational excellence
C. Reliability
D. Security''',
     'respuesta': 'C. Reliability',
     'argumento': 'The Reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it’s expected to. This includes the ability to operate and test the workload through its total lifecycle. This paper provides in-depth, best practice guidance for implementing reliable workloads on AWS.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html'},
    {'pregunta': 'Which AWS tool acts as a firewall to control traffic in and out of subnets within a VPC?',
     'opciones': '''A. Security group
B. Route table
C. VPC endpoint
D. Network access control list (ACL)''',
     'respuesta': 'D. Network access control list (ACL)',
     'argumento': 'A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level. You can use the default network ACL for your VPC, or you can create a custom network ACL for your VPC with rules that are similar to the rules for your security groups in order to add an additional layer of security to your VPC.',
     'referencia': 'https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html'},
    {'pregunta': 'A company is running a standard PostgreSQL database on premises. The company is migrating the database to the AWS Cloud and does not want to change the queries that access the database. The company must maximize the query performance. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon RDS for PostgreSQL
B. Amazon Aurora PostgreSQL
C. Amazon DocumentDB (with MongoDB compatibility)
D. Amazon DynamoDB''',
     'respuesta': 'A. Amazon RDS for PostgreSQL',
     'argumento': 'Aurora is fully compatible with MySQL and PostgreSQL, allowing existing applications and tools to run without requiring modification. Testing on standard benchmarks such as SysBench has shown an increase in throughput of up to 5x over stock MySQL and 3x over stock PostgreSQL on similar hardware. Aurora uses a variety of software and hardware techniques to ensure the database engine is able to fully use available compute, memory, and networking. I/O operations use distributed systems techniques, such as quorums to improve performance consistency.',
     'referencia': 'https://aws.amazon.com/rds/aurora/features/#Migration_Support'}, #375
    {'pregunta': 'A company needs to use machine learning and pattern matching to identify and protect sensitive data that the company stores in the AWS Cloud. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon Inspector
B. Amazon Macie
C. Amazon GuardDuty
D. AWS Audit Manager''',
     'respuesta': 'B. Amazon Macie',
     'argumento': 'Amazon Macie is a data security service that uses machine learning (ML) and pattern matching to discover and help protect your sensitive data.',
     'referencia': 'https://aws.amazon.com/macie/'},
    {'pregunta': 'A company wants to offer direct phone and chat channels for customer service. The company needs a pay-as-you-go solution that remote customer service agents can use to create and manage voice and chat contact flows. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon EventBridge (Amazon CloudWatch Events)
B. Amazon Connect
C. Amazon Cognito
D. AWS Direct Connect''',
     'respuesta': 'B. Amazon Connect',
     'argumento': 'Amazon Connect is a pay-as-you-go cloud contact center. There are no required minimum monthly fees, long-term commitments, or upfront license charges, and pricing is not based on peak capacity, agent seats, or maintenance; you only pay for what you use. Amazon Connect offers capabilities for your contact center and agent workspace, including forecasting, capacity planning, and scheduling and outbound campaigns, as well as Voice, Chat, Tasks, Customer Profiles, Contact Lens, Voice ID, Wisdom, and Cases, and Guides.',
     'referencia': 'https://aws.amazon.com/connect/pricing/'},
    {'pregunta': 'A company has acquired several other companies. All the companies host their IT infrastructure in the AWS Cloud. Which AWS service should the acquiring company use to centralize the account management?',
     'opciones': '''A. AWS Systems Manager
B. AWS Organizations
C. AWS Security Hub
D. Amazon Workspaces''',
     'respuesta': 'B. AWS Organizations',
     'argumento': 'AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html'},
    {'pregunta': 'A company is using AWS for all its IT infrastructure. The company´s developers are allowed to deploy applications on their own. The developers want to deploy their applications without having to provision the infrastructure themselves. Which AWS service should the developers use to meet these requirements?',
     'opciones': '''A. AWS Cloud Formation
B. AWS CodeBuild
C. AWS Elastic Beanstalk
D. AWS CodeDeploy''',
     'respuesta': 'C. AWS Elastic Beanstalk',
     'argumento': 'AWS Elastic Beanstalk makes it even easier for developers to quickly deploy and manage applications in the AWS Cloud. Developers simply upload their application, and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring.',
     'referencia': 'https://aws.amazon.com/elasticbeanstalk/faqs/'},
    {'pregunta': 'A company needs to analyze its AWS Cloud environment to determine whether the company is following security best practices. The company wants recommendations about how to close security gaps. Which AWS service should the company use to obtain these recommendations?',
     'opciones': '''A. AWS WAF
B. AWS Systems Manager
C. AWS Trusted Advisor
D. AWS Shield''',
     'respuesta': 'C. AWS Trusted Advisor',
     'argumento': 'AWS Trusted Advisor provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas. You can then follow the recommendations to optimize your services and resources. AWS Basic Support and AWS Developer Support customers can access core security checks and checks for service quotas. AWS Business Support and AWS Enterprise Support customers can access all checks, including cost optimization, security, fault tolerance, performance, and service quotas. For a complete list of checks and descriptions, see the Trusted Advisor Best Practices.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/'}, #380
    {'pregunta': 'A company is using AWS Identity and Access Management (IAM). Who can manage the access keys of the AWS account root user?',
     'opciones': '''A. IAM users in the same account that have been granted permission
B. IAM roles in any account that have been granted permission
C. IAM users and roles that have been granted permission
D. The AWS account owner''',
     'respuesta': 'D. The AWS account owner',
     'argumento': '',
     'referencia': 'https://docs.aws.amazon.com/accounts/latest/reference/root-user-access-key.html'},
    {'pregunta': 'A company needs a managed NFS file system that the company can use with its AWS compute resources. Which AWS service or feature will meet these requirements?',
     'opciones': '''A. Amazon Elastic Block Store (Amazon EBS)
B. AWS Storage Gateway Tape Gateway
C. Amazon S3 Glacier Flexible Retrieval
D. Amazon Elastic File System (Amazon EFS)''',
     'respuesta': 'D. Amazon Elastic File System (Amazon EFS)',
     'argumento': 'Amazon Elastic File System (EFS) is designed to provide serverless, fully elastic file storage that lets you share file data without provisioning or managing storage capacity and performance. An Amazon EFS file system grows and shrinks automatically as you add and remove files, so you don’t need to manage storage procurement or provisioning.',
     'referencia': 'https://aws.amazon.com/efs/faq/'},
    {'pregunta': 'What is the security best practice concerning sensitive data stored in Amazon S3?',
     'opciones': '''A. Enable cross-Region replication on the S3 bucket.
B. Enable S3 server-side encryption on the S3 bucket.
C. Configure AWS WAF to prevent unauthorized access to the S3 bucket.
D. Configure Amazon GuardDuty to prevent unauthorized access to the S3 bucket.''',
     'respuesta': 'B. Enable S3 server-side encryption on the S3 bucket.',
     'argumento': 'Server-side encryption – When you use server-side encryption, Amazon S3 encrypts your objects before saving them on disks in its data centers and then decrypts the objects when you download them. Server-side encryption can help reduce risk to your data by encrypting the data with a key that is stored in a different mechanism than the mechanism that stores the data itself.',
     'referencia': 'https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html#:~:text=Server%2Dside%20encryption%20%E2%80%93%20When,stores%20the%20data%20itself.'},
    {'pregunta': 'An application requires a database that offers consistent performance and latency that can be measured in single-digit milliseconds. Which AWS service meets these requirements?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Redshift
D. Amazon EMR''',
     'respuesta': 'A. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is designed to run high-performance, internet-scale applications that would overburden traditional relational databases. With over ten years of pioneering innovation investment, Amazon DynamoDB offers limitless scalability with consistent single-digit millisecond performance and up to 99.999% availability.',
     'referencia': 'https://aws.amazon.com/dynamodb/features/#Performance_at_scale'},
    {'pregunta': 'A company needs to block SQL injection attacks. Which AWS service or feature provides this functionality?',
     'opciones': '''A. AWS WAF
B. Network ACLs
C. Security groups
D. AWS Trusted Advisor''',
     'respuesta': 'A. AWS WAF',
     'argumento': 'AWS WAF is a web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) web requests based on conditions that you define. These conditions include IP addresses, HTTP headers, HTTP body, URI strings, SQL injection and cross-site scripting.',
     'referencia': 'https://aws.amazon.com/waf/faqs/'}, #385
    {'pregunta': 'A company wants its Amazon EC2 instances to operate in a highly available environment, even if there is a natural disaster in a particular geographic area. Which solution achieves this goal?',
     'opciones': '''A. Use EC2 instances in a single Availability Zone
B. Use EC2 instances in multiple AWS Regions
C. Use EC2 instances in multiple edge locations.
D. Use Amazon CloudFront with the EC2 instances configured as the source.''',
     'respuesta': 'B. Use EC2 instances in multiple AWS Regions',
     'argumento': 'Using EC2 instances in multiple AWS Regions ensures high availability even in the event of a natural disaster in a particular geographic area. If one region goes down due to a disaster, the instances in other regions will continue to function normally, providing uninterrupted service to customers. This solution provides a higher level of fault tolerance and disaster recovery capability, as compared to using EC2 instances in a single Availability Zone or multiple edge locations.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/39/'},
    {'pregunta': 'Treating infrastructure as code in the AWS Cloud allows users to:',
     'opciones': '''A. automate migration of on-premises hardware to AWS data centers.
B. let a third party automate an audit of the AWS infrastructure.
C. turn over application code to AWS so it can run on the AWS infrastructure.
D. automate the infrastructure provisioning process.''',
     'respuesta': 'D. automate the infrastructure provisioning process.',
     'argumento': 'Practicing infrastructure as code means applying the same rigor of application code development to infrastructure provisioning. All configurations should be defined in a declarative way and stored in a source control system such as AWS CodeCommit, the same as application code. Infrastructure provisioning, orchestration, and deployment should also support the use of the infrastructure as code.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html'},
    {'pregunta': 'A company needs to apply security rules to specific Amazon EC2 instances. Which AWS service or feature provides this functionality?',
     'opciones': '''A. AWS WAF
B. Network ACLs
C. Amazon VPC
D. Security groups''',
     'respuesta': 'D. Security groups',
     'argumento': 'A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don´t specify a security group, Amazon EC2 uses the default security group for the VPC. You can add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time. New and modified rules are automatically applied to all instances that are associated with the security group. When Amazon EC2 decides whether to allow traffic to reach an instance, it evaluates all of the rules from all of the security groups that are associated with the instance.',
     'referencia': 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html'},
    {'pregunta': 'A company wants to run Amazon EC2 instances in locations that are near the company’s global users. Which aspect of the AWS environment will support this requirement?',
     'opciones': '''A. Availability Zone
B. Edge locations
C. AWS Regions
D. Regional edge caches''',
     'respuesta': 'C. AWS Regions',
     'argumento': 'AWS Regions are geographically dispersed locations where AWS infrastructure is available. Each region is designed to be isolated from other regions, so that you can run your applications and store your data in a location that is close to your global users.',
     'referencia': 'https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/using-regions-and-availability-zones.html'},
    {'pregunta': 'A company´s project team needs to simultaneously mount a file system on multiple Amazon EC2 Linux instances. The file system also will be shared across multiple Availability Zones. Which AWS service will meet these requirements?',
     'opciones': '''A. Amazon Elastic File System (Amazon EFS)
B. Amazon S3
C. Amazon Elastic Block Store (Amazon EBS)
D. Amazon FSx for Windows File Server''',
     'respuesta': 'A. Amazon Elastic File System (Amazon EFS)',
     'argumento': 'Amazon Elastic File System (Amazon EFS) is a fully managed file storage service that allows you to create and mount a file system on multiple Amazon EC2 Linux instances simultaneously. It also allows you to share the file system across multiple Availability Zones, making it ideal for applications that need to maintain high availability.',
     'referencia': 'https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html'}, #390
    {'pregunta': 'A large retail company wants to use an AWS service to process clickstream data from the company´s ecommerce website. The company wants to collect and analyze the streaming data in real time. Which AWS service meets these requirements?',
     'opciones': '''A. Amazon Kinesis
B. Amazon Athena
C. Amazon CloudFront
D. AWS Data Exchange''',
     'respuesta': 'A. Amazon Kinesis',
     'argumento': 'Amazon Kinesis is a fully managed service that allows you to collect, process, and analyze streaming data in real-time. This service can be used to process clickstream data from an ecommerce website in real-time.',
     'referencia': 'https://www.metricfire.com/integrations/amazon-cloudfront/amazon-kinesis/'},
    {'pregunta': 'Which pillar of the AWS Well-Architected Framework focuses on the return on investment of moving into the AWS Cloud?',
     'opciones': '''A. Sustainability
B. Cost optimization
C. Operational excellence
D. Reliability''',
     'respuesta': 'B. Cost optimization',
     'argumento': 'Analyze and attribute expenditure: The cloud makes it easier to accurately identify the usage and cost of systems, which then allows transparent attribution of IT costs to individual workload owners. This helps measure return on investment (ROI) and gives workload owners an opportunity to optimize their resources and reduce costs.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html'},
    {'pregunta': 'A company is developing an application that the company will host on Amazon EC2 instances. The application must be available 24 hours a day, 7 days a week. The company needs a scalable, highly available cloud architecture to support the application. Which guidelines should the company apply in its design to meet these requirements? (Choose two.)',
     'opciones': '''A. Use EC2 Spot Instances
B. Use Multi-AZ deployments.
C. Use Auto Scaling groups
D. Use AWS Backup.
E. Use EC2 Reserved Instances.''',
     'respuesta': '''B. Use Multi-AZ deployments. 
C. Use Auto Scaling groups''',
     'argumento': 'B. Use Multi-AZ deployments: Multi-AZ deployments allow the company to run the application across multiple availability zones within a region. This provides high availability and automatic failover in the event of a failure in one availability zone. C. Use Auto Scaling groups: Auto Scaling groups allow the company to automatically add or remove Amazon EC2 instances based on the demand for the application, which is important for ensuring high availability and scalability.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/use-multiple-availability-zones.html, https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/dynamic-scaling-with-aws-lambda-amazon-route-53-and-aws-auto-scaling.html'},
    {'pregunta': 'Which AWS service helps users audit API activity across their AWS account?',
     'opciones': '''A. AWS CloudTrail
B. Amazon Inspector
C. AWS WAF
D. AWS Config''',
     'respuesta': 'A. AWS CloudTrail',
     'argumento': 'CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs, continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.',
     'referencia': 'https://aws.amazon.com/cloudtrail/faqs/#:~:text=CloudTrail%20enables%20auditing%2C%20security%20monitoring,%2C%20analysis%2C%20and%20remediation%20actions.'},
    {'pregunta': 'Which AWS service should a company use to create a serverless workflow?',
     'opciones': '''A. Amazon Connect
B. AWS Lambda
C. AWS Step Functions
D. Amazon Elastic Block Store (Amazon EBS)
E. AWS CodeBuild''',
     'respuesta': 'C. AWS Step Functions',
     'argumento': 'Step Functions is a serverless orchestration service that lets you easily coordinate multiple Lambda functions into flexible workflows that are easy to debug and change. Step Functions will keep your Lambda functions free of additional logic by triggering and tracking each step of your application for you.',
     'referencia': 'https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/'}, #395
    {'pregunta': 'A company wants to build a data analytics application that uses Amazon Redshift. The company needs a cost estimate for its future Amazon Redshift usage. Which AWS tool will provide a high-level cost estimation?',
     'opciones': '''A. AWS Budgets
B. AWS Pricing Calculator
C. AWS Cost Explorer
D. Saving Plans''',
     'respuesta': 'B. AWS Pricing Calculator',
     'argumento': '',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/40/'},
    {'pregunta': 'A company is using Amazon EC2 instances. Which tasks are the company´s responsibility, according to the AWS shared responsibility model? (Choose two.)',
     'opciones': '''A. Choose the initial root password of new Linux instances.
B. Identify which users can access the EC2 instances, and manage their permissions in the operating system.
C. Apply the updates of the hypervisor where the EC2 instances are running.
D. Choose between a Wi-Fi connection and an Ethernet connection for the global internet access.
E. Identify and manage the users who are allowed to create or delete EC2 instances.''',
     'respuesta': '''B. Identify which users can access the EC2 instances, and manage their permissions in the operating system. 
E. Identify and manage the users who are allowed to create or delete EC2 instances.''',
     'argumento': 'B. Identify which users can access the EC2 instances, and manage their permissions in the operating system. This includes managing the security group rules, and managing access control mechanisms such as AWS Identity and Access Management (IAM) policies. E. Identify and manage the users who are allowed to create or delete EC2 instances. This includes creating, modifying, or deleting IAM policies and roles.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/40/'},
    {'pregunta': 'Which AWS service gives users the ability to run AWS services on premises?',
     'opciones': '''A. Amazon CloudFront
B. AWS Outposts
C. AWS Global Accelerator
D. Amazon VPC''',
     'respuesta': 'B. AWS Outposts',
     'argumento': 'An Outpost is a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region. You can create subnets on your Outpost and specify them when you create AWS resources such as EC2 instances, EBS volumes, ECS clusters, and RDS instances.',
     'referencia': 'https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html'},
    {'pregunta': 'Which guideline is a well-architected design principle tor building cloud applications?',
     'opciones': '''A. Keep static data closer to compute resources.
B. Provision resources for peak capacity.
C. Design for automated recovery from failure.
D. Use tightly coupled components.''',
     'respuesta': 'C. Design for automated recovery from failure.',
     'argumento': '',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html'},
    {'pregunta': 'Which actions are examples of a company´s effort to rightsize its AWS resources to control cloud costs? (Choose two.)',
     'opciones': '''A. Switch from Amazon RDS to Amazon DynamoDB to accommodate NoSQL datasets.
B. Base the selection of Amazon EC2 instance types on past utilization patterns.
C. Use Amazon S3 Lifecycle policies to move objects that users access infrequently to lower-cost storage tiers.
D. Use Multi-AZ deployments for Amazon RDS.
E. Replace existing Amazon EC2 instances with AWS Elastic Beanstalk.''',
     'respuesta': '''B. Base the selection of Amazon EC2 instance types on past utilization patterns. 
C. Use Amazon S3 Lifecycle policies to move objects that users access infrequently to lower-cost storage tiers.''',
     'argumento': 'Right sizing is the process of matching instance types and sizes to your workload performance and capacity requirements at the lowest possible cost. It’s also the process of looking at deployed instances and identifying opportunities to eliminate or downsize without compromising capacity or other requirements, which results in lower costs. Right sizing is a key mechanism for optimizing AWS costs, but it is often ignored by organizations when they first move to the AWS Cloud. They lift and shift their environments and expect to right size later. Speed and performance are often prioritized over cost, which results in oversized instances and a lot of wasted spend on unused resources',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/'}, #400
    {'pregunta': 'Where can AWS users review answers to frequently asked questions about security in the AWS Cloud?',
     'opciones': '''A. AWS Trusted Advisor
B. AWS Knowledge Center
C. AWS Support Center
D. AWS Artifact''',
     'respuesta': 'B. AWS Knowledge Center',
     'argumento': 'AWS re:Post includes AWS Official Knowledge Center articles and videos covering the most frequent questions and requests that we receive from AWS customers.',
     'referencia': 'https://repost.aws/knowledge-center'},
    {'pregunta': 'Which AWS service or feature can a company use to estimate AWS costs before provisioning workloads?',
     'opciones': '''A. AWS Pricing Calculator
B. AWS Cost and Usage Report
C. Cost Explorer
D. AWS Budgets''',
     'respuesta': 'A. AWS Pricing Calculator',
     'argumento': 'AWS Pricing Calculator is a web-based planning tool that you can use to create estimates for your AWS use cases. You can use it to model your solutions before building them, explore the AWS service price points, and review the calculations behind your estimates. You can use it to help you plan how you spend, find cost saving opportunities, and make informed decisions when using Amazon Web Services. AWS Pricing Calculator is useful for those who have never used AWS. It´s also useful for those who want to reorganize or expand their AWS usage. You don´t need any experience with the cloud or AWS to use AWS Pricing Calculator.',
     'referencia': 'https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html'},
    {'pregunta': 'An application that is hosted on Amazon EC2 has a steady and consistent workload. The application will operate for at least 1 year. What is the MOST cost-effective instance purchasing option to meet these requirements?',
     'opciones': '''A. Spot Instances
B. Reserved Instances
C. On-Demand Instances
D. Dedicated Hosts''',
     'respuesta': 'C. On-Demand Instances',
     'argumento': 'To meet the requirements of having a steady and consistent workload on an Amazon EC2 instance that will operate for at least 1 year, the most cost-effective instance purchasing option is Reserved Instances (RIs).',
     'referencia': 'https://blogs.vmware.com/cloudhealth/aws-reserved-instances-vs-on-demand/#:~:text=The%20difference%20between%20Reserved%20Instances%20and%20On%20Demand&text=The%20only%20difference%20between%20the,of%20an%20On%20Demand%20instance.'},
    {'pregunta': 'A company needs to use dashboards and charts to analyze insights from business data. Which AWS service will provide the dashboards and charts for these insights?',
     'opciones': '''A. Amazon Macie
B. Amazon Aurora
C. Amazon QuickSight
D. AWS CloudTrail''',
     'respuesta': 'C. Amazon QuickSight',
     'argumento': 'Amazon QuickSight is a very fast, easy-to-use, cloud-powered business analytics service that makes it easy for all employees within an organization to build visualizations, perform ad-hoc analysis, and quickly get business insights from their data, anytime, on any device. ',
     'referencia': 'https://aws.amazon.com/quicksight/resources/faqs/'},
    {'pregunta': 'Which of the following are security principles in the AWS Well-Architected Framework? (Choose two.)',
     'opciones': '''A. Analyze and attribute expenditures.
B. Monitor, alert, and audit actions and changes to AWS resources.
C. Deploy globally in minutes.
D. Protect data in transit and at rest.
E. Perform operations as code.''',
     'respuesta': '''A. Monitor, alert, and audit actions and changes to AWS resources. 
D. Protect data in transit and at rest.''',
     'argumento': 'his principle is important to detect and respond to security incidents by monitoring and alerting on security-related events, and by auditing changes to AWS resources. This principle is important to protect data from unauthorized access, disclosure, alteration, or destruction, both when it is moving across networks and when it is stored.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/security.html'}, #405
    {'pregunta': 'A company moves its infrastructure from on premises to the AWS Cloud. The company can now provision additional Amazon EC2 instances whenever the instances are required. With this ability, the company can launch new marketing campaigns in 3 days instead of 3 weeks. Which benefit of the AWS Cloud does this scenario demonstrate?',
     'opciones': '''A. Cost savings
B. Improved operational resilience
C. Increased business agility
D. Enhanced security''',
     'respuesta': 'C. Increased business agility',
     'argumento': 'Increase speed and agility – In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'A company wants to design a reliable web application that is hosted on Amazon EC2. Which approach will achieve this goal?',
     'opciones': '''A. Launch large EC2 instances in the same Availability Zone
B. Spread EC2 instances across more than one security group
C. Spread EC2 instances across more than one Availability Zone.
D. Use an Amazon Machine Image (AMI) from AWS Marketplace.''',
     'respuesta': 'C. Spread EC2 instances across more than one Availability Zone.',
     'argumento': 'This mentions reliability, which is part of the AWS Well architected framework. Which means been able to automatically recover from failures, therefor, we need more availability zones.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/41/'},
    {'pregunta': 'Which AWS service should a company use to provision, manage, and deploy SSL/TLS certificates?',
     'opciones': '''A. AWS Secrets Manager
B. Amazon Inspector
C. AWS CodeDeploy
D. AWS Certificate Manager (ACM)''',
     'respuesta': 'D. AWS Certificate Manager (ACM)',
     'argumento': 'Use AWS Certificate Manager (ACM) to provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services and your internal connected resources. ACM removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.',
     'referencia': 'https://aws.amazon.com/certificate-manager/'},
    {'pregunta': 'A company provides Amazon Workspaces to its remote employees. The company wants to prevent employees from using their virtual desktops to visit specific websites that are known to be malicious. Which AWS service should the company use to meet this requirement?',
     'opciones': '''A. AWS Shield Advanced
B. Amazon Route 53
C. Amazon GuardDuty
D. AWS Network Firewall''',
     'respuesta': 'D. AWS Network Firewall',
     'argumento': 'Network Firewall’s flexible rules engine lets you define firewall rules that give you fine-grained control over network traffic, such as blocking outbound Server Message Block (SMB) requests to prevent the spread of malicious activity.',
     'referencia': 'https://aws.amazon.com/network-firewall/faqs/'},
    {'pregunta': 'A company wants to build an application that uses AWS Lambda to run Python code. Under the AWS shared responsibility model, which tasks will be the company´s responsibility? (Choose two.)',
     'opciones': '''A. Management of the underlying infrastructure
B. Management of the operating system.
C. Writing the business logic code.
D. Installation of the computer language runtime.
E. Providing AWS Identity and Access Management (1AM) access to the Lambda service.''',
     'respuesta': '''C. Writing the business logic code. 
E. Providing AWS Identity and Access Management (1AM) access to the Lambda service.''',
     'argumento': 'The customer is responsible for writing the business logic code that will be executed by AWS Lambda. They are also responsible for providing IAM access to the Lambda service, so that the Lambda function can access other AWS resources.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/41/'}, #410
    {'pregunta': 'Which of the following is one of the pillars of the AWS Well-Architected Framework?',
     'opciones': '''A. Efficiency and redundancy
B. High availability
C. Operational excellence
D. Business optimization''',
     'respuesta': 'C. Operational excellence',
     'argumento': 'Built around six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs.',
     'referencia': 'https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc'},
    {'pregunta': 'A company has multiple departments. The company must charge each department for its exact AWS Cloud usage, including data transfer costs. How can the company determine these costs by department?',
     'opciones': '''A. Use one AWS account for each department.
B. Use cost allocation tags on services that are used the most often.
C. Use AWS Trusted Advisor.
D. Use Savings Plans.''',
     'respuesta': 'A. Use one AWS account for each department.',
     'argumento': 'Cost allocation tags are labels that can be applied to AWS resources to categorize and track their costs. By using cost allocation tags, the company can identify which resources are being used by each department and allocate the costs accordingly. Using one AWS account for each department (option A) would provide isolation and separation of resources, but it may not be the most cost-effective solution, as each account incurs additional charges.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/42/'},
    {'pregunta': 'An ecommerce company has Amazon EC2 instances running as web servers. There is a predictable pattern of peak traffic load that occurs two times each day, always at the same time. The EC2 instances are idle for the remainder of the day. What is the MOST cost-effective way to manage these resources while maintaining fault tolerance?',
     'opciones': '''A. Use an Auto Scaling group to scale resources in and out based on demand.
B. Purchase Reserved Instances to ensure peak capacity at all times.
C. Write a cron job to stop the EC2 instances when the traffic demand is low.
D. Write a script to vertically scale the EC2 instances during peak traffic demand.''',
     'respuesta': 'A. Use an Auto Scaling group to scale resources in and out based on demand.',
     'argumento': 'The most cost-effective way to manage the resources while maintaining fault tolerance is to use an Auto Scaling group. This will automatically scale the number of Amazon EC2 instances up or down based on demand.',
     'referencia': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html'},
    {'pregunta': 'A company wants to integrate its online shopping website with social media login credentials. Which AWS service can the company use to make this integration?',
     'opciones': '''A. AWS Directory Service
B. AWS Identity and Access Management (IAM)
C. Amazon Cognito
D. AWS IAM Identity Center (AWS Single Sign-On)''',
     'respuesta': 'C. Amazon Cognito',
     'argumento': 'With Amazon Cognito, you can add user sign-up and sign-in features and control access to your web and mobile applications. Amazon Cognito provides an identity store that scales to millions of users, supports social and enterprise identity federation, and offers advanced security features to protect your consumers and business. Built on open identity standards, Amazon Cognito supports various compliance regulations and integrates with frontend and backend development resources.',
     'referencia': 'https://aws.amazon.com/cognito/'},
    {'pregunta': 'A company needs to create graphs that show historical and current costs for the company´s AWS account. Which AWS service or tool provides this functionality?',
     'opciones': '''A. AWS Config
B. AWS Cost and Usage Report
C. AWS Budgets
D. AWS Cost Explorer''',
     'respuesta': 'D. AWS Cost Explorer',
     'argumento': 'AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. Get started quickly by creating custom reports that analyze cost and usage data. Analyze your data at a high level (for example, total costs and usage across all accounts), or dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-cost-explorer/'}, #415
    {'pregunta': 'A company acquired another corporation. The company now has two AWS accounts. Which AWS service or tool can the company use to consolidate the billing for these two accounts?',
     'opciones': '''A. AWS Systems Manager
B. AWS Organizations
C. AWS License Manager
D. Cost Explorer''',
     'respuesta': 'B. AWS Organizations',
     'argumento': 'AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html'},
    {'pregunta': 'Which AWS Support plans provide a complete set of AWS Trusted Advisor checks?',
     'opciones': '''A. AWS Business Support and AWS Basic Support
B. AWS Enterprise Support and AWS Business Support
C. AWS Enterprise Support and AWS Developer Support
D. AWS Business Support and AWS Developer Support''',
     'respuesta': 'B. AWS Enterprise Support and AWS Business Support',
     'argumento': 'AWS Trusted Advisor is a service that provides a set of best practices and recommendations for AWS customers to optimize their AWS usage and reduce costs. The complete set of Trusted Advisor checks is available with the AWS Enterprise Support and AWS Business Support plans. These plans provide a complete set of checks across all categories, including security, performance, and cost optimization.',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/'},
    {'pregunta': 'Which of the following is a method for building a highly available application on AWS?',
     'opciones': '''A. Place an Independent copy of the application in two or more Availability Zones.
B. Place codependent components of the application in two or more Availability Zones
C. Run one version of the application in one Availability Zone and run an earlier version of the application in a second Availability Zone.
D. Deploy two copies of the application in a single Availability Zone.''',
     'respuesta': 'A. Place an Independent copy of the application in two or more Availability Zones.',
     'argumento': '',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/42/'},
    {'pregunta': 'Which statement is an AWS Cloud best practice that focuses on the elasticity and agility of cloud computing?',
     'opciones': '''A. Provision capacity based on past usage and theoretical peaks.
B. Dynamically scale to meet usage demands.
C. Build the application and infrastructure in a data center that grants physical access.
D. Break apart the application into loosely coupled components.''',
     'respuesta': 'B. Dynamically scale to meet usage demands.',
     'argumento': 'Elasticity focuses on the ability to automatically scale resources based on demand. This helps you to optimize your resources and reduce costs, while still ensuring that your applications have the resources they need to run smoothly. Whereas Agility focuses on the speed and ease of allocating and deallocating resources. This allows for vast amounts of computing resources to be provisioned in a matter of minutes, making it easier for you to respond to changing business needs.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.elasticity.en.html'},
    {'pregunta': 'Which AWS service could an administrator use to provide desktop environments for several employees?',
     'opciones': '''A. AWS Organizations
B. AWS Fargate
C. AWS WAF
D. AWS Workspaces''',
     'respuesta': 'D. AWS Workspaces',
     'argumento': 'Amazon WorkSpaces offers an easy way to provide a cloud-based desktop experience to your end users.',
     'referencia': 'https://docs.aws.amazon.com/workspaces/index.html'}, #420
    {'pregunta': 'A company simulates workflows to review and validate that all processes are effective and that staff are familiar with the processes. Which design principle of the AWS Well-Architected Framework is the company following with this practice?',
     'opciones': '''A. Perform operations as code.
B. Refine operation procedures frequently.
C. Make frequent, small, reversible changes.
D. Structure the company to support business outcomes.''',
     'respuesta': 'B. Refine operation procedures frequently.',
     'argumento': 'Refine operations procedures frequently: As you use operations procedures, look for opportunities to improve them. As you evolve your workload, evolve your procedures appropriately. Set up regular game days to review and validate that all procedures are effective and that teams are familiar with them.',
     'referencia': 'https://wa.aws.amazon.com/wat.pillar.operationalExcellence.en.html'},
    {'pregunta': 'Which AWS services or resources can a company use directly on its on-premises servers? (Choose two.)',
     'opciones': '''A. AWS OpsWorks
B. AWS CloudFormation
C. AWS Storage Gateway
D. Application Load Balancer
E. Amazon Cognito''',
     'respuesta': '''A. AWS OpsWorks.
C. AWS Storage Gateway''',
     'argumento': 'AWS OpsWorks is a configuration management service that allows you to manage applications and server configurations. It supports on-premises servers in addition to AWS instances. This means you can use AWS OpsWorks to manage and deploy applications on your own on-premises servers. AWS Storage Gateway is a hybrid cloud storage service that enables on-premises applications to seamlessly use AWS cloud storage. It acts as a bridge between your on-premises environment and AWS cloud storage services like Amazon S3 and Amazon Glacier. By using AWS Storage Gateway, you can extend your storage infrastructure to the cloud without directly using AWS resources in your on-premises servers.',
     'referencia': 'https://aws.amazon.com/opsworks/?nc2=type_a#:~:text=OpsWorks%20lets%20you%20use%20Chef%20and%20Puppet%20to%20automate%20how%20servers%20are%20configured%2C%20deployed%2C%20and%20managed%20across%20your%20Amazon%20EC2%20instances%20or%20on%2Dpremises%20compute%20environments.'},
    {'pregunta': 'According to the AWS shared responsibility model, the customer is responsible for applying the latest security updates and patches for which of the following?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon EC2 instances
C. Amazon RDS instances
D. Amazon S3''',
     'respuesta': 'B. Amazon EC2 instances',
     'argumento': '',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/43/'},
    {'pregunta': 'Which cloud computing advantage is a company applying when it uses AWS Regions to increase application availability to users in different countries?',
     'opciones': '''A. Pay-as-you-go pricing
B. Capacity forecasting
C. Economies of scale
D. Global reach''',
     'respuesta': 'D. Global reach',
     'argumento': 'Go global in minutes – Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at minimal cost.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'Which option is an advantage of AWS Cloud computing that minimizes variable costs?',
     'opciones': '''A. High availability
B. Economies of scale
C. Global reach
D. Agility''',
     'respuesta': 'B. Economies of scale',
     'argumento': 'Benefit from massive economies of scale – By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'}, #425
    {'pregunta': 'Which action will help increase security in the AWS Cloud?',
     'opciones': '''A. Enable programmatic access for all IAM users.
B. Use IAM users instead of IAM roles to delegate permissions.
C. Rotate access keys on a reoccurring basis.
D. Use inline policies instead of customer managed policies.''',
     'respuesta': 'C. Rotate access keys on a reoccurring basis.',
     'argumento': 'Regularly rotating long-term credentials helps you familiarize yourself with the process. This is useful in case you are ever in a situation where you must rotate credentials, such as when an employee leaves your company. We recommend that you use IAM access last used information to rotate and remove access keys safely',
     'referencia': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials'},
    {'pregunta': 'A user wants to transport data between AWS and an on-premises environment using a private network connection. Which AWS service or feature can be used to meet these requirements?',
     'opciones': '''A. NAT gateway
B. AWS Direct Connect
C. Amazon VPC
D. Internet gateway''',
     'respuesta': 'B. AWS Direct Connect',
     'argumento': 'AWS Direct Connect is a networking service that provides an alternative to using the internet to connect to AWS. Using AWS Direct Connect, data that would have previously been transported over the internet is delivered through a private network connection between your facilities and AWS. In many circumstances, private network connections can reduce costs, increase bandwidth, and provide a more consistent network experience than internet-based connections.',
     'referencia': 'https://aws.amazon.com/directconnect/faqs/?nc=sn&loc=6'},
    {'pregunta': 'Which AWS service can serve a static website?',
     'opciones': '''A. Amazon S3
B. Amazon Route 53
C. Amazon QuickSight
D. AWS X-Ray''',
     'respuesta': 'A. Amazon S3',
     'argumento': 'You can use Amazon S3 to host a static website. On a static website, individual webpages include static content. They might also contain client-side scripts. By contrast, a dynamic website relies on server-side processing, including server-side scripts, such as PHP, JSP, or ASP.NET. Amazon S3 does not support server-side scripting, but AWS has other resources for hosting dynamic websites.',
     'referencia': 'https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html'},
    {'pregunta': 'Which design principles are enabled by the AWS Cloud to improve the operation of workloads? (Choose two.)',
     'opciones': '''A. Minimize upfront design
B. Loose coupling
C. Disposable resources
D. Server design and concurrency
E. Minimal viable product''',
     'respuesta': '''B. Loose coupling. 
C. Disposable resources''',
     'argumento': 'B. Loose coupling: This principle refers to the ability to design and operate the different components of a workload independently of each other, so that changes in one component do not affect the others. This allows for more flexibility and scalability in the design and operation of the workload. C. Disposable resources: This principle refers to the ability to quickly and easily provision, scale, and dispose of resources as needed. This allows for more efficient use of resources and can improve the overall cost-effectiveness of the workload.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/43/'},
    {'pregunta': 'A large company has a workload that requires hardware to remain on premises. The company wants to use the same management and control plane services that it currently uses on AWS. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. AWS Device Farm
B. AWS Fargate
C. AWS Outposts
D. AWS Ground Station''',
     'respuesta': 'C. AWS Outposts',
     'argumento': 'Truly consistent hybrid experience Use the same hardware infrastructure, APIs, tools, and management controls available in the cloud to provide a truly consistent developer and IT operations experience.',
     'referencia': 'https://aws.amazon.com/outposts/'}, #430
    {'pregunta': 'Which of the following is included within the security pillar of the AWS Well-Architected Framework?',
     'opciones': '''A. Identity federation
B. Data protection
C. Incident reporting
D. Disaster recovery''',
     'respuesta': 'B. Data protection',
     'argumento': '',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-dataprot.html'},
    {'pregunta': 'A company has been storing monthly reports in an Amazon S3 bucket. The company exports the report data into comma-separated values (.csv) files. A developer wants to write a simple query that can read all of these files and generate a summary report. Which AWS service or feature should the developer use to meet these requirements with the LEAST amount of operational overhead?',
     'opciones': '''A. Amazon S3 Select
B. Amazon Athena
C. Amazon Redshift
D. Amazon EC2''',
     'respuesta': 'B. Amazon Athena',
     'argumento': 'Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. The developer can use it to write a simple query that can read all of the .csv files in the Amazon S3 bucket and generate a summary report. Athena uses Presto, an open-source query engine, to perform the queries, and it does not require any infrastructure to be provisioned or managed. This means that the developer can use it with the least amount of operational overhead.',
     'referencia': 'https://aws.amazon.com/blogs/aws/amazon-athena-interactive-sql-queries-for-data-in-amazon-s3/'},
    {'pregunta': 'A company wants the ability to accommodate peak application usage without purchasing equipment for on-premises data centers. Which AWS Cloud benefit is the company seeking?',
     'opciones': '''A. High availability
B. Security
C. Reliability
D. Elasticity''',
     'respuesta': 'D. Elasticity',
     'argumento': 'Elasticity is the ability of a system to automatically provision and de-provision resources based on the changing workload demands. AWS provides a variety of services that can be scaled up or down quickly and automatically, allowing companies to adjust their computing resources as needed to accommodate fluctuations in application usage. This means that companies can avoid over-provisioning resources and paying for unused capacity, and also can handle peak workloads without purchasing additional hardware.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.elasticity.en.html'},
    {'pregunta': 'Which of the following are pillars of the AWS Well-Architected Framework? (Choose two.)',
     'opciones': '''A. Availability
B. Reliability
C. Scalability
D. Responsive design
E. Operational excellence''',
     'respuesta': '''B. Reliability. 
E. Operational excellence''',
     'argumento': 'The Well-Architected Framework is based on six pillars: Operational excellence. Security. Reliability. Performance efficiency. Cost optimization. Sustainability',
     'referencia': 'https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc'},
    {'pregunta': 'Which AWS service provides highly durable object storage?',
     'opciones': '''A. Amazon S3
B. Amazon Elastic File System (Amazon EFS)
C. Amazon Elastic Block Store (Amazon EBS)
D. Amazon FSx''',
     'respuesta': 'A. Amazon S3',
     'argumento': 'Amazon S3 is object storage built to store and retrieve any amount of data from anywhere. S3 is a simple storage service that offers industry leading durability, availability, performance, security, and virtually unlimited scalability at very low costs.',
     'referencia': 'https://aws.amazon.com/s3/faqs/?nc=sn&loc=7'}, #435
    {'pregunta': 'A company needs to migrate all of its development teams to a cloud-based integrated development environment (IDE). Which AWS service should the company use?',
     'opciones': '''A. AWS CodeBuild
B. AWS Cloud9
C. AWS OpsWorks
D. AWS Cloud Development Kit (AWS CDK)''',
     'respuesta': 'B. AWS Cloud9',
     'argumento': 'AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, Python, PHP, and more, so you don’t need to install files or configure your development machine to start new projects.',
     'referencia': 'https://aws.amazon.com/cloud9/'},
    {'pregunta': 'Which AWS database service providers in-memory data storage?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon ElastiCache
C. Amazon RDS
D. Amazon Timestream''',
     'respuesta': 'B. Amazon ElastiCache',
     'argumento': 'Amazon ElastiCache is a web service that makes it easy to deploy, operate, and scale an in-memory data store or cache in the cloud.',
     'referencia': 'https://aws.amazon.com/nosql/in-memory/, https://aws.amazon.com/nosql/in-memory/#:~:text=Amazon%20ElastiCache%20for%20Memcached&text=ElastiCache%20for%20Memcached%20is%20fully,Tech%2C%20and%20E%2DCommerce.'},
    {'pregunta': 'A company needs a content delivery network that provides secure delivery of data, videos, applications, and APIs to users globally with low latency and high transfer speeds. Which AWS service meets these requirements?',
     'opciones': '''A. Amazon CloudFront
B. Elastic Load Balancing
C. Amazon S3
D. Amazon Elastic Transcoder''',
     'respuesta': 'A. Amazon CloudFront',
     'argumento': 'Amazon CloudFront is a web service that gives businesses and web application developers an easy and cost effective way to distribute content with low latency and high data transfer speeds. Like other AWS services, Amazon CloudFront is a self-service, pay-per-use offering, requiring no long term commitments or minimum fees. With CloudFront, your files are delivered to end-users using a global network of edge locations.',
     'referencia': 'https://aws.amazon.com/cloudfront/faqs/?nc=sn&loc=5&dn=2'},
    {'pregunta': 'Which of the following are design principles for reliability in the AWS Cloud? (Choose two.)',
     'opciones': '''A. Build architectures with tightly coupled resources.
B. Use AWS Trusted Advisor to meet security best practices.
C. Use automation to recover immediately from failure.
D. Right size Amazon EC2 instances to ensure optimal performance.
E. Simulate failures to test recovery processes.''',
     'respuesta': '''C. Use automation to recover immediately from failure. 
E. Simulate failures to test recovery processes.''',
     'argumento': 'Manage change in automation: Changes to your infrastructure should be made using automation. The changes that need to be managed include changes to the automation, which then can be tracked and reviewed. Test recovery procedures: In an on-premises environment, testing is often conducted to prove that the workload works in a particular scenario. Testing is not typically used to validate recovery strategies. In the cloud, you can test how your workload fails, and you can validate your recovery procedures.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html'},
    {'pregunta': 'Which AWS service is a cloud security posture management (CSPM) service that aggregates alerts from various AWS services and partner products in a standardized format?',
     'opciones': '''A. AWS Security Hub
B. AWS Trusted Advisor
C. Amazon EventBridge
D. Amazon GuardDuty''',
     'respuesta': 'A. AWS Security Hub',
     'argumento': 'AWS Security Hub is a cloud security posture management (CSPM) service that performs security best practice checks, aggregates alerts, and enables automated remediation. Use AWS Security Hub to automate security best practice checks, aggregate security alerts into a single place and format, and understand your overall security posture across all of your AWS accounts.',
     'referencia': 'https://aws.amazon.com/security-hub/'}, #440
    {'pregunta': 'A company wants to use the AWS Cloud to define its entire infrastructure as code. The company wants to limit human error and activate consistent responses to events. Which pillar of the AWS Well-Architected Framework does this plan support?',
     'opciones': '''A. Security
B. Operational excellence
C. Cost optimization
D. Reliability''',
     'respuesta': 'B. Operational excellence',
     'argumento': 'Perform operations as code: In the cloud, you can apply the same engineering discipline that you use for application code to your entire environment. You can define your entire workload (applications, infrastructure) as code and update it with code. You can implement your operations procedures as code and automate their run process by initiating them in response to events. By performing operations as code, you limit human error and achieve consistent responses to events.',
     'referencia': 'https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html'},
    {'pregunta': 'A developer wants AWS users to access AWS services by using temporary security credentials. Which AWS service or feature should the developer use to provide these credentials?',
     'opciones': '''A. IAM policies
B. IAM user groups
C. AWS Security Token Service (AWS STS)
D. AWS IAM Identity Center (AWS Single Sign-On)''',
     'respuesta': 'C. AWS Security Token Service (AWS STS)',
     'argumento': 'AWS provides AWS Security Token Service (AWS STS) as a web service that enables you to request temporary, limited-privilege credentials for users.',
     'referencia': 'https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html'},
    {'pregunta': 'Which of the following is an architectural design principle of the AWS Well-Architected Framework?',
     'opciones': '''A. Loosely couple components
B. Build monolithic systems
C. Scale vertically, not horizontally
D. Use third-party software''',
     'respuesta': 'A. Loosely couple components',
     'argumento': 'loosely coupling components, is a key architectural design principle of the AWS Well-Architected Framework. It involves designing systems so that the components are decoupled and can operate independently of each other. This allows for greater flexibility, scalability, and resilience, and reduces the risk of cascading failures.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/45/'},
    {'pregunta': 'What does the Amazon S3 Intelligent-Tiering storage class offer?',
     'opciones': '''A. Payment flexibility by reserving storage capacity
B. Long-term retention of data by copying the data to an encrypted Amazon Elastic Block Store (Amazon EBS) volume
C. Automatic cost savings by moving objects between tiers based on access pattern changes
D. Secure, durable, and lowest cost storage for data archival''',
     'respuesta': 'C. Automatic cost savings by moving objects between tiers based on access pattern changes',
     'argumento': 'Amazon S3 Intelligent-Tiering storage class is designed for data with unknown or changing access patterns. It automatically moves objects between two access tiers: the frequent access tier and the infrequent access tier. This allows for automatic cost savings as the system moves objects to the appropriate tier based on access patterns. Objects that are infrequently accessed will automatically be moved to the infrequent access tier, which has a lower cost per GB-month, while objects that are frequently accessed will remain in the frequent access tier. It does not offer payment flexibility by reserving storage capacity or long-term retention of data by copying the data to an encrypted Amazon Elastic Block Store (Amazon EBS) volume or Secure, durable, and lowest cost storage for data archival.',
     'referencia': 'https://aws.amazon.com/s3/storage-classes/intelligent-tiering/'},
    {'pregunta': 'How does the AWS Cloud help companies build agility into their processes and cloud infrastructure?',
     'opciones': '''A. Companies can avoid provisioning too much capacity when they do not know how much capacity is required.
B. Companies can expand into new geographic regions.
C. Companies can access a range of technologies to experiment and innovate quickly.
D. Companies can pay for IT resources only when they use the resources.''',
     'respuesta': 'C. Companies can access a range of technologies to experiment and innovate quickly.',
     'argumento': 'Increase speed and agility – In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'}, #445
    {'pregunta': 'Which of the following is a recommended design principle of the AWS Well-Architected Framework?',
     'opciones': '''A. Reduce downtime by making infrastructure changes infrequently and in large increments.
B. Invest the time to configure infrastructure manually.
C. Learn to improve from operational failures.
D. Use monolithic application design for centralization.''',
     'respuesta': 'C. Learn to improve from operational failures.',
     'argumento': 'Learn from all operational failures: Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html'},
    {'pregunta': 'An Availability Zone consists of:',
     'opciones': '''A. one or more data centers in a single location.
B. two or more data centers in multiple locations.
C. one or more physical hosts in a single data center.
D. two or more physical hosts in multiple data centers.''',
     'respuesta': 'B. two or more data centers in multiple locations.',
     'argumento': 'Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html'},
    {'pregunta': 'A company is designing a web application that will run on Amazon EC2 instances. Which AWS services and features will improve availability and reduce the impact of failures for this application? (Choose two.)',
     'opciones': '''A. Amazon EC2 Auto Scaling for the EC2 instances
B. VPC subnet ACLs to check the health of a service
C. Resources that are distributed across multiple Availability Zones
D. Configuration of AWS Server Migration Service (AWS SMS) to move the EC2 instances to a different AWS Region
E. Resources that are distributed across multiple AWS points of presence''',
     'respuesta': '''A. Amazon EC2 Auto Scaling for the EC2 instances. 
C. Resources that are distributed across multiple Availability Zones''',
     'argumento': 'Amazon EC2 Auto Scaling: This service automatically increases or decreases the number of Amazon EC2 instances in response to changes in demand for the application. Resources that are distributed across multiple Availability Zones: By distributing the application resources across multiple Availability Zones, you can protect your application from the failure of a single data center.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/45/'},
    {'pregunta': 'Which fully managed AWS service assists with the creation, testing, and management of custom Amazon EC2 images?',
     'opciones': '''A. EC2 Image Builder
B. Amazon Machine Image (AMI)
C. AWS Launch Wizard
D. AWS Elastic Beanstalk''',
     'respuesta': 'A. EC2 Image Builder',
     'argumento': 'EC2 Image Builder simplifies the building, testing, and deployment of Virtual Machine and container images for use on AWS or on-premises. Image Builder significantly reduces the effort of keeping images up-to-date and secure by providing a simple graphical interface, built-in automation, and AWS-provided security settings. With Image Builder, there are no manual steps for updating an image nor do you have to build your own automation pipeline.',
     'referencia': 'https://aws.amazon.com/image-builder/'},
    {'pregunta': 'Which of the following describes an AWS Region?',
     'opciones': '''A. Specific location within a geographic area that provides high availability
B. Set of data centers spanning multiple countries
C. A global picture of a user's cloud computing environment
D. A collection of databases that can be accessed from a specific geographic area only''',
     'respuesta': 'A. Specific location within a geographic area that provides high availability',
     'argumento': 'AWS Regions consist of multiple, physically separated and isolated Availability Zones that are connected with low latency, high throughput, highly redundant networking',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/45/'}, #450
    {'pregunta': 'Which AWS service provides recommendations to help users optimize costs and follow AWS best practices?',
     'opciones': '''A. AWS Trusted Advisor
B. AWS Service Catalog
C. AWS Ground Station
D. Amazon GuardDuty''',
     'respuesta': 'A. AWS Trusted Advisor',
     'argumento': 'AWS Trusted Advisor provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/'},
    {'pregunta': 'Which AWS service provides a cloud-based contact center that scales to support a business of any size?',
     'opciones': '''A. Amazon Personalize
B. Amazon Cognito
C. Amazon Connect
D. Amazon Lightsail''',
     'respuesta': 'C. Amazon Connect',
     'argumento': 'With Amazon Connect, you can set up a contact center in minutes that can scale to support millions of customers.',
     'referencia': 'https://aws.amazon.com/connect/'},
    {'pregunta': 'A financial company needs to centrally manage its AWS accounts and use consolidated billing. Which AWS service or feature should the company use?',
     'opciones': '''A. AWS Cost Explorer
B. AWS Organizations
C. AWS Billing and Cost Management
D. AWS Budgets''',
     'respuesta': 'B. AWS Organizations',
     'argumento': 'AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.',
     'referencia': 'https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html'},
    {'pregunta': 'A company is preparing for an audit and wants documentation that AWS complies with the Payment Card Industry Data Security Standard (PCI DSS). Where can the company find this documentation?',
     'opciones': '''A. AWS Artifact
B. AWS Organizations
C. AWS Trusted Advisor
D. AWS Support Center''',
     'respuesta': 'A. AWS Artifact',
     'argumento': 'The PCI DSS Attestation of Compliance (AOC) and Responsibility Summary is available to customers through AWS Artifact, a self-service portal for on-demand access to AWS compliance reports. Sign in to AWS Artifact in the AWS Management Console, or learn more at Getting Started with AWS Artifact.',
     'referencia': 'https://aws.amazon.com/compliance/pci-dss-level-1-faqs/'},
    {'pregunta': 'A company stores data in an Amazon S3 bucket. Which task is the responsibility of AWS?',
     'opciones': '''A. Configure an S3 Lifecycle policy.
B. Activate S3 Versioning.
C. Configure S3 bucket policies.
D. Protect the infrastructure that supports S3 storage.''',
     'respuesta': 'D. Protect the infrastructure that supports S3 storage.',
     'argumento': 'AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. The effectiveness of our security is regularly tested and verified by third-party auditors as part of the AWS compliance programs',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/46/'}, #455
    {'pregunta': 'Which AWS service allows a user to provision a managed MySQL DB instance?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon Redshift
C. Amazon RDS
D. AWS Database Migration Service (AWS DMS)''',
     'respuesta': 'C. Amazon RDS',
     'argumento': 'Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. Choose from seven popular engines — Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server — and deploy on-premises with Amazon RDS on AWS Outposts.',
     'referencia': 'https://aws.amazon.com/rds/'},
    {'pregunta': 'Which AWS service should a cloud practitioner use to receive real-time guidance for provisioning resources, based on AWS best practices related to security, cost optimization, and service limits?',
     'opciones': '''A. AWS Trusted Advisor
B. AWS Config
C. AWS Security Hub
D. AWS Systems Manager''',
     'respuesta': 'A. AWS Trusted Advisor',
     'argumento': 'AWS Trusted Advisor provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas. You can then follow the recommendations to optimize your services and resources.',
     'referencia': 'https://aws.amazon.com/premiumsupport/technology/trusted-advisor/'},
    {'pregunta': 'Which statements represent the cost-effectiveness of the AWS Cloud? (Choose two.)',
     'opciones': '''A. Users can trade fixed expenses for variable expenses.
B. Users can deploy all over the world in minutes.
C. AWS offers increased speed and agility.
D. AWS is responsible for patching the infrastructure.
E. Users benefit from economies of scale.''',
     'respuesta': '''A. Users can trade fixed expenses for variable expenses. 
E. Users benefit from economies of scale.''',
     'argumento': 'using the AWS Cloud allows users to pay only for the resources they consume, rather than investing in expensive on-premises hardware and software. AWS Cloud provides massive economies of scale, meaning that the cost of running infrastructure is distributed across a vast number of users. This results in lower prices for users as compared to running their own infrastructure.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/46/'},
    {'pregunta': 'Which AWS service stores graph data in the form of vertices and edges?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon RDS
C. Amazon Quantum Ledger Database (Amazon QLDB)
D. Amazon Neptune''',
     'respuesta': 'D. Amazon Neptune',
     'argumento': 'Amazon Neptune is a fully managed database service built for the cloud that makes it easier to build and run graph applications. Neptune provides built-in security, continuous backups, serverless compute, and integrations with other AWS services.',
     'referencia': 'https://aws.amazon.com/neptune/'},
    {'pregunta': 'When designing AWS workloads to be operational even when there are component failures, what is an AWS best practice?',
     'opciones': '''A. Perform quarterly disaster recovery tests.
B. Place the main component on the us-east-1 Region.
C. Design for automatic failover to healthy resources.
D. Design workloads to fit on a single Amazon EC2 instance.''',
     'respuesta': 'C. Design for automatic failover to healthy resources.',
     'argumento': 'REL 11: How do you design your workload to withstand component failures? Best Practices: Fail over to healthy resources: Ensure that if a resource failure occurs, that healthy resources can continue to serve requests.',
     'referencia': 'https://wa.aws.amazon.com/wat.question.REL_11.en.html'}, #460
    {'pregunta': 'A company wants to protect resources that the company hosts on AWS, including Application Load Balancers and Amazon CloudFront distributions. The company wants an AWS service that can provide near real-time visibility into attacks on the company´s resources. The service must also have a dedicated AWS team to assist with distributed denial of service (DDoS) attacks. Which AWS service will meet these requirements?',
     'opciones': '''A. AWS WAF
B. AWS Shield Standard
C. Amazon Macie
D. AWS Shield Advanced''',
     'respuesta': 'D. AWS Shield Advanced',
     'argumento': 'AWS Shield Advanced protection provides always-on, flow-based monitoring of network traffic and active application monitoring to provide near real-time notifications of suspected DDoS incidents. AWS Shield Advanced also employs advanced attack mitigation and routing techniques for automatically mitigating attacks. Customers with Business or Enterprise support can also engage the Shield Response Team (SRT) 24x7 to manage and mitigate their application layer DDoS attacks.',
     'referencia': 'https://aws.amazon.com/shield/faqs/#:~:text=AWS%20Shield%20Advanced%20protection,application%20layer%20DDoS%20attacks.'},
    {'pregunta': 'Which AWS Support plan provides customers with access to an AWS technical account manager (TAM)?',
     'opciones': '''A. AWS Basic Support
B. AWS Developer Support
C. AWS Business Support
D. AWS Enterprise Support''',
     'respuesta': 'D. AWS Enterprise Support',
     'argumento': 'Designated Technical Account Manager (TAM) to proactively monitor your environment and assist with optimization and coordinate access to programs and AWS experts',
     'referencia': 'https://aws.amazon.com/premiumsupport/plans/#:~:text=Designated%20Technical%20Account%20Manager%20(TAM)%20to%20proactively%20monitor%20your%20environment%20and%20assist%20with%20optimization%20and%20coordinate%20access%20to%20programs%20and%20AWS%20experts'},
    {'pregunta': 'Which task is the responsibility of a company that is using Amazon RDS?',
     'opciones': '''A. Provision the underlying infrastructure.
B. Create IAM policies to control administrative access to the service.
C. Install the cables to connect the hardware for compute and storage.
D. Install and patch the RDS operating system.''',
     'respuesta': 'B. Create IAM policies to control administrative access to the service.',
     'argumento': 'The company´s AWS account owner or administrator is responsible for setting up the necessary IAM policies to control access to the RDS resources.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/47/'},
    {'pregunta': 'A company has an application with robust hardware requirements. The application must be accessed by students who are using lightweight, low-cost laptops. Which AWS service will help the company deploy the application without investing in backend infrastructure or high-end client hardware?',
     'opciones': '''A. Amazon AppStream 2.0
B. AWS AppSync
C. Amazon WorkLink
D. AWS Elastic Beanstalk''',
     'respuesta': 'A. Amazon AppStream 2.0',
     'argumento': 'AppStream 2.0 lets you move your desktop applications to AWS without rewriting them. It’s easy to install your applications on AppStream 2.0, set launch configurations, and make your applications available to users. AppStream 2.0 offers a wide selection of configuration options so you can select the instance type and auto-scale parameters that best match your application and end-user requirements. AppStream 2.0 allows you to launch applications in your own network, which means your applications can interact with your existing AWS resources.',
     'referencia': 'https://aws.amazon.com/appstream2/faqs/?nc=sn&loc=7'},
    {'pregunta': 'Which of the following is an AWS value proposition that describes a user´s ability to scale infrastructure based on demand?',
     'opciones': '''A. Speed of innovation
B. Resource elasticity
C. Decoupled architecture
D. Global deployment''',
     'respuesta': 'B. Resource elasticity',
     'argumento': 'Most people, when thinking of cloud computing, think of the ease with which they can procure resources when needed. This is only one aspect to elasticity. The other aspect is to contract when they no longer need resources. Scale out and scale in. Scale up and scale down. Some services do this as part of their service: Amazon S3, Amazon SQS, Amazon SNS, Amazon SES, Amazon Aurora, etc. Some require vertical scaling, like Amazon RDS. Others integrate with AWS Auto Scaling, like Amazon EC2, Amazon ECS, AWS Fargate, Amazon EKS, and Amazon DynamoDB. Amazon Aurora Serverless and Amazon Athena also qualify as elastic.',
     'referencia': 'https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.elasticity.en.html'}, #465
    {'pregunta': 'A company needs to organize its resources and track AWS costs on a detailed level. The company needs to categorize costs by business department, environment, and application. Which solution will meet these requirements?',
     'opciones': '''A. Access the AWS Cost Management console to organize resources, set an AWS budget, and receive notifications of unintentional usage.
B. Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level.
C. Create Amazon CloudWatch dashboards to visually organize and track costs individually.
D. Access the AWS Billing and Cost Management dashboard to organize and track resource consumption on a detailed level.''',
     'respuesta': 'B. Use tags to organize the resources. Activate cost allocation tags to track AWS costs on a detailed level.',
     'argumento': 'Your organization´s financial governance might require transparent accounting of costs incurred at the application, business unit, cost center, and team level. Performing cost attribution supported by Cost Allocation Tags provides you the data necessary to accurately attribute the costs incurred by an entity from appropriately tagged resources.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/cost-allocation-tags.html'},
    {'pregunta': 'Using Amazon Elastic Container Service (Amazon ECS) to break down a monolithic architecture into microservices is an example of:',
     'opciones': '''A. a loosely coupled architecture.
B. a tightly coupled architecture.
C. a stateless architecture.
D. a stateful architecture.''',
     'respuesta': 'A. a loosely coupled architecture.',
     'argumento': 'Service independence increases an application’s resistance to failure. In a monolithic architecture, if a single component fails, it can cause the entire application to fail. With microservices, applications handle total service failure by degrading functionality and not crashing the entire application.',
     'referencia': 'https://aws.amazon.com/microservices/#:~:text=code%20from%20scratch.-,Resilience,-Service%20independence%20increases'},
    {'pregunta': 'Which AWS benefit is demonstrated by on-demand technology services that enable companies to replace upfront fixed expenses with variable expenses?',
     'opciones': '''A. High availability
B. Economies of scale
C. Pay-as-you-go pricing
D. Global reach''',
     'respuesta': 'C. Pay-as-you-go pricing',
     'argumento': 'AWS offers you a pay-as-you-go approach for pricing for the vast majority of our cloud services. With AWS you pay only for the individual services you need, for as long as you use them, and without requiring long-term contracts or complex licensing. AWS pricing is similar to how you pay for utilities like water and electricity. You only pay for the services you consume, and once you stop using them, there are no additional costs or termination fees.',
     'referencia': 'https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all'},
    {'pregunta': 'Which AWS service is a key-value database that provides sub-millisecond latency on a large scale?',
     'opciones': '''A. Amazon DynamoDB
B. Amazon Aurora
C. Amazon DocumentDB (with MongoDB compatibility)
D. Amazon Neptune''',
     'respuesta': 'A. Amazon DynamoDB',
     'argumento': 'Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.',
     'referencia': 'https://aws.amazon.com/dynamodb/'},
    {'pregunta': 'A company stores several terabytes of data in an Amazon S3 bucket. The company needs to query the data by using standard SQL and does not want to set up infrastructure. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. Amazon RDS
B. Amazon Redshift
C. Amazon Athena
D. Amazon EC2''',
     'respuesta': 'C. Amazon Athena',
     'argumento': 'Athena is an interactive analytics service that makes it simple to analyze data in Amazon Simple Storage Service (S3) using Python. Athena is serverless, so there is no infrastructure to set up or manage, and you can start analyzing data immediately. You don’t even need to load your data into Athena; it works directly with data stored in Amazon S3. ',
     'referencia': 'https://aws.amazon.com/athena/faqs/?nc=sn&loc=6'}, #470
    {'pregunta': 'Which AWS service supports the analysis, investigation, and identification of the root cause of security events and suspicious activities in an AWS account?',
     'opciones': '''A. Amazon Inspector
B. Amazon Macie
C. Amazon Detective
D. Amazon CloudWatch''',
     'respuesta': 'C. Amazon Detective',
     'argumento': 'Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities.',
     'referencia': 'https://aws.amazon.com/it/detective/features/#:~:text=Amazon%20Detective%20makes%20it%20easy,security%20issues%20or%20suspicious%20activities.'},
    {'pregunta': 'A company plans to run its IT infrastructure in the AWS Cloud. The infrastructure must be highly available. The company also must minimize the network latency between servers. Which deployment scenario will meet these requirements?',
     'opciones': '''A. Deploy in multiple Availability Zones in multiple AWS Regions.
B. Deploy in one Availability Zone in one AWS Region
C. Deploy in multiple AWS Regions. Deploy in one Availability Zone in each Region.
D. Deploy in multiple Availability Zones in one AWS Region.''',
     'respuesta': 'D. Deploy in multiple Availability Zones in one AWS Region.',
     'argumento': 'The infrastructure must be highly available. Should the compamy use multiple Availability Zones. The company also must minimize the network latency between servers. should be in one AWS Region.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/48/'},
    {'pregunta': 'Which AWS service decouples application components so that the components run independently?',
     'opciones': '''A. Amazon Simple Notification Service (Amazon SNS)
B. Amazon Simple Workflow Service (Amazon SWF)
C. AWS Glue
D. Amazon Simple Queue Service (Amazon SQS)''',
     'respuesta': 'D. Amazon Simple Queue Service (Amazon SQS)',
     'argumento': 'Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service provided by AWS. It enables you to decouple and scale microservices, distributed systems, and serverless applications by allowing different components or services to communicate asynchronously through message queues.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/48/'},
    {'pregunta': 'A company is designing an application. For the data persistence layer, the company wants to use a NoSQL database. Which AWS service should the company use for the database?',
     'opciones': '''A. Amazon Redshift
B. AWS DataSync
C. Amazon Athena
D. Amazon DynamoDB''',
     'respuesta': 'D. Amazon DynamoDB',
     'argumento': '',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/48/'},
    {'pregunta': 'Which AWS service keeps track of SSL/TLS certificates, creates new certificates, and processes renewals?',
     'opciones': '''A. AWS Identity and Access Management (IAM)
B. AWS Certificate Manager (ACM)
C. AWS Config
D. AWS Trusted Advisor''',
     'respuesta': 'B. AWS Certificate Manager (ACM)',
     'argumento': 'Use AWS Certificate Manager (ACM) to provision, manage, and deploy public and private SSL/TLS certificates for use with AWS services and your internal connected resources. ACM removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.',
     'referencia': 'https://aws.amazon.com/certificate-manager/'}, #475
    {'pregunta': 'A company is using AWS Lambda. Which task is the company’s responsibility, according to the AWS shared responsibility model?',
     'opciones': '''A. Update the Lambda runtime language.
B. Maintain the runtime environment.
C. Maintain the networking infrastructure.
D. Configure the resource.''',
     'respuesta': 'D. Configure the resource.',
     'argumento': 'According to the AWS shared responsibility model, the company is responsible for configuring the resources that they create in AWS Lambda, such as setting up the function, defining the function´s triggers, specifying the function´s runtime settings, and granting permissions to the function.',
     'referencia': 'https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/the-shared-responsibility-model.html'},
    {'pregunta': 'A company needs to process data from satellite communications without managing any infrastructure. Which AWS service should the company use to meet these requirements?',
     'opciones': '''A. Amazon CloudWatch
B. Amazon Aurora
C. Amazon Athena
D. AWS Ground Station''',
     'respuesta': 'D. AWS Ground Station',
     'argumento': 'AWS Ground Station is a fully managed service that lets you control satellite communications, process data, and scale your operations without having to worry about building or managing your own ground station infrastructure. Satellites are used for a wide variety of use cases, including weather forecasting, surface imaging, communications, and video broadcasts.',
     'referencia': 'https://aws.amazon.com/ground-station/'},
    {'pregunta': 'A company wants to run its applications in the AWS Cloud. The company does not have enough staff to maintain and protect its critical business applications. Which AWS service should the company use to perform these tasks?',
     'opciones': '''A. AWS Shield
B. Amazon RDS
C. AWS Config
D. AWS Managed Services (AMS)''',
     'respuesta': 'D. AWS Managed Services (AMS)',
     'argumento': 'AMS extends your team with operational capabilities including monitoring, incident management, AWS Incident Detection and Response, security, patch, backup, and cost optimization.',
     'referencia': 'https://aws.amazon.com/managed-services/#:~:text=AMS%20extends%20your%20team%20with%20operational%20capabilities%20including%20monitoring%2C%20incident%20management%2C%20AWS%20Incident%20Detection%20and%20Response%2C%20security%2C%20patch%2C%20backup%2C%20and%20cost%20optimization.'},
    {'pregunta': 'A company needs to test a new application that was written in Python. The code will activate when new images are stored in an Amazon S3 bucket. The application will put a watermark on each image and then will store the images in a different S3 bucket. Which AWS service should the company use to conduct the test with the LEAST amount of operational overhead?',
     'opciones': '''A. Amazon EC2
B. AWS Code Deploy
C. AWS Lambda
D. Amazon Lightsail''',
     'respuesta': 'C. AWS Lambda',
     'argumento': '',
     'referencia': 'https://aws.amazon.com/blogs/architecture/convert-and-watermark-documents-automatically-with-amazon-s3-object-lambda/'},
    {'pregunta': 'A cloud engineer needs to track AWS costs. The cloud engineer also needs to receive event driven alerts when costs exceed specific thresholds. Which AWS tool provides this functionality?',
     'opciones': '''A. AWS Cost Explorer
B. AWS Budgets
C. Cost allocation tags
D. AWS Cost and Usage Reports''',
     'respuesta': 'B. AWS Budgets',
     'argumento': 'Using AWS Budgets, you can set a budget that alerts you when you exceed (or are forecasted to exceed) your budgeted cost or usage amount. You can also set alerts based on your RI or Savings Plans Utilization and Coverage using AWS Budgets.',
     'referencia': 'https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/'}, #480
    {'pregunta': 'Which of the following is available to a company that has an AWS Business Support plan?',
     'opciones': '''A. AWS Support concierge
B. AWS DDoS Response Team (DRT)
C. AWS technical account manager (TAM)
D. AWS Health API''',
     'respuesta': 'D. AWS Health API',
     'argumento': 'The AWS technical account manager (TAM) is on AWS Enterprise Support',
     'referencia': 'https://aws.amazon.com/es/premiumsupport/plans/enterprise/'},
    {'pregunta': 'A company wants to migrate its on-premises data warehouse to AWS. The information in the data warehouse is used to populate analytics dashboards. Which AWS service should the company use for the data warehouse?',
     'opciones': '''A. Amazon ElastiCache
B. Amazon Aurora
C. Amazon RDS
D. Amazon Redshift''',
     'respuesta': 'D. Amazon Redshift',
     'argumento': 'Tens of thousands of customers today rely on Amazon Redshift to analyze exabytes of data and run complex analytical queries, making it a widely used cloud data warehouse. Run and scale analytics in seconds on all your data without having to manage your data warehouse infrastructure.',
     'referencia': 'https://aws.amazon.com/redshift/#:~:text=to%20Amazon%20Redshift-,Tens%20of%20thousands%20of%20customers%20today%20rely%20on%20Amazon%20Redshift,manage%20your%20data%20warehouse%20infrastructure.'},
    {'pregunta': 'A company wants to use machine learning to identify suspicious activities in its AWS account. Which AWS service provides this functionality?',
     'opciones': '''A. AWS Shield
B. Amazon Macie
C. Amazon Detective
D. AWS WAF''',
     'respuesta': 'C. Amazon Detective',
     'argumento': 'Amazon Detective makes it easier to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.',
     'referencia': 'https://aws.amazon.com/detective/faqs/'},
    {'pregunta': 'A company is hosting a web application in a Docker container on Amazon EC2. AWS is responsible for which of the following tasks?',
     'opciones': '''A. Scaling the web application and services developed with Docker
B. Provisioning or scheduling containers to run on clusters and maintain their availability
C. Performing hardware maintenance in the AWS facilities that run the AWS Cloud
D. Managing the guest operating system, including updates and security patches''',
     'respuesta': 'C. Performing hardware maintenance in the AWS facilities that run the AWS Cloud',
     'argumento': 'AWS responsibility "Security of the Cloud" - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.',
     'referencia': 'https://aws.amazon.com/compliance/shared-responsibility-model/'},
    {'pregunta': 'Which options does AWS make available for customers who want to learn about security in the cloud in an instructor-led setting? (Choose two.)',
     'opciones': '''A. AWS Trusted Advisor
B. AWS Online Tech Talks
C. AWS Blog
D. AWS Forums
E. AWS Classroom Training''',
     'respuesta': '''B. AWS Online Tech Talks. 
E. AWS Classroom Training''',
     'argumento': 'AWS Online Tech Talks cover a wide range of topics and expertise levels through technical deep dives, demos, customer examples, and live Q&A with AWS experts. AWS Classroom Training offers live classes with instructors who teach you in-demand cloud skills and best practices using a mix of presentations, discussion, and hands-on labs.',
     'referencia': 'https://aws.amazon.com/events/online-tech-talks/?events-master-ott.sort-by=item.additionalFields.startDate&events-master-ott.sort-order=asc&awsf.event-type=*all&awsf.series=*all&awsf.category=*all&awsf.level=*all, https://aws.amazon.com/training/classroom/ '}, #485
    {'pregunta': 'Which AWS service will help a company identify the user who deleted an Amazon EC2 instance yesterday?',
     'opciones': '''A. Amazon CloudWatch
B. AWS Trusted Advisor
C. AWS CloudTrail
D. Amazon Inspector''',
     'respuesta': 'C. AWS CloudTrail',
     'argumento': 'AWS CloudTrail monitors and records account activity across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.',
     'referencia': 'https://aws.amazon.com/cloudtrail/?nc1=h_ls'},
    {'pregunta': 'A company is configuring its AWS Cloud environment. The company´s administrators need to group users together and apply permissions to the group. Which AWS service or feature can the company use to meet these requirements?',
     'opciones': '''A. AWS Organizations
B. Resource groups
C. Resource tagging
D. AWS Identity and Access Management (IAM)''',
     'respuesta': 'D. AWS Identity and Access Management (IAM)',
     'argumento': 'AWS Identity and Access Management (IAM) roles provide a way to access AWS by relying on temporary security credentials. Each role has a set of permissions for making AWS service requests, and a role is not associated with a specific user or group.',
     'referencia': 'https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/49/'},
    {'pregunta': 'Which statement describes a characteristic of the AWS global infrastructure?',
     'opciones': '''A. Edge locations contain multiple AWS Regions
B. AWS Regions contain multiple Regional edge caches
C. Availability Zones contain multiple data centers
D. Each data center contains multiple edge locations''',
     'respuesta': 'C. Availability Zones contain multiple data centers',
     'argumento': 'An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region.',
     'referencia': 'https://aws.amazon.com/about-aws/global-infrastructure/regions_az/'},
    {'pregunta': 'A company has an online shopping website and wants to store customers credit card data. The company must meet Payment Card Industry (PCI) standards. Which service can the company use to access AWS compliance documentation?',
     'opciones': '''A. Amazon Cloud Directory
B. AWS Artifact
C. AWS Trusted Advisor
D. Amazon Inspector''',
     'respuesta': 'B. AWS Artifact',
     'argumento': 'AWS Artifact, available in the console, is a self-service audit artifact retrieval portal that provides our customers with on-demand access to AWS’ compliance documentation and AWS agreements. You can use AWS Artifact Reports to download AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and System and Organization Control (SOC) reports.',
     'referencia': 'https://aws.amazon.com/artifact/faq/'},
    {'pregunta': 'Which AWS service can a company use to perform complex analytical queries?',
     'opciones': '''A. Amazon RDS
B. Amazon DynamoDB
C. Amazon Redshift
D. Amazon ElastiCache''',
     'respuesta': 'C. Amazon Redshift',
     'argumento': 'ens of thousands of customers today rely on Amazon Redshift to analyze exabytes of data and run complex analytical queries, making it a widely used cloud data warehouse. Run and scale analytics in seconds on all your data without having to manage your data warehouse infrastructure.',
     'referencia': 'https://aws.amazon.com/redshift/'}, #490
]

