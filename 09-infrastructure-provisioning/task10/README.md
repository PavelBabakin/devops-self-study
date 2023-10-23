# Task 10: Use CloudFormation change sets to preview changes before applying them.

AWS CloudFormation change sets provide a powerful mechanism to preview how proposed changes to a stack might impact your resources before actual implementation. This ensures safe and predictable stack updates, allowing developers to understand the implications of their changes in a risk-free manner. In this guide, we will explore how to create and use CloudFormation change sets to preview and manage changes to our stacks.

---

**Step 1: Understanding CloudFormation Change Sets**

1. **What is a Change Set?**
    - A summary of proposed changes to a stack that you can review before deciding to apply them.
2. **Why Use Change Sets?**
    - To preview and understand changes.
    - To prevent unintentional resource modifications or deletions.

---

**Step 2: Creating a Basic CloudFormation Stack**

Before we explore change sets, let’s assume we have a basic CloudFormation stack deployed, such as an S3 bucket.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A basic CloudFormation template to create an S3 bucket.

Resources:
  MyS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: my-sample-s3-bucket
```

---

**Step 3: Modifying the Stack**

Suppose we want to add versioning to our S3 bucket. Before applying the change, we will use a change set to preview the modifications.

Modified template:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A modified CloudFormation template to enable S3 bucket versioning.

Resources:
  MyS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: my-sample-s3-bucket
      VersioningConfiguration:
        Status: Enabled
```

---

**Step 4: Creating a Change Set via AWS Management Console**

1. **Navigate to CloudFormation:**
    - Open the AWS Management Console and select “CloudFormation”.
2. **Select the Stack:**
    - Choose the stack you want to update.
3. **Create Change Set:**
    - Click “Update” and then select “Replace current template”.
    - Upload the modified template and click “Next”.
    - Configure stack options and click “Next”.
    - On the “Review” page, click “Create change set”.
4. **Review Changes:**
    - Examine the changes listed in the change set.
    - Note the “Action” column which indicates whether a resource will be added, modified, or removed.

---

**Step 5: Creating a Change Set via AWS CLI**

1. **Create Change Set:**
    - Use the following AWS CLI command:
        
        ```bash
        aws cloudformation create-change-set --stack-name MyS3BucketStack --template-body file://path_to_modified_template.yaml --change-set-name MyChangeSet
        ```
        
2. **Describe Change Set:**
    - Use the following command to view the changes:
        
        ```bash
        aws cloudformation describe-change-set --stack-name MyS3BucketStack --change-set-name MyChangeSet
        ```
        

---

**Step 6: Executing or Deleting the Change Set**

1. **Execute the Change Set:**
    - If you’re satisfied with the previewed changes, execute the change set to apply the modifications.
2. **Delete the Change Set:**
    - If you decide not to proceed with the changes, delete the change set to discard the proposed modifications.

---

**Conclusion**

Utilizing AWS CloudFormation change sets allows developers to preview, understand, and manage changes to their stacks, ensuring safe and controlled stack updates. By leveraging change sets, developers can prevent unintended consequences, ensuring the stability and reliability of their AWS environments.

In the upcoming articles, we will explore more advanced CloudFormation topics, such as working with nested stacks, using AWS CloudFormation Macros, and managing stack drift. Join us as we continue to explore the extensive capabilities of AWS CloudFormation!