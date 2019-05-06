# (S3) seoul region에서 각 region까지의 latency

  1. S3에 15개의 가용 region에 bucket을 만든다.
  2. AWS IAM을 이용하여 KEY를 발급받는다.
  3. AWS CLI 환경 구축하기
  4. Python BOTO3를 이용하여 코드를 작성한다.
  5. 각 bucket에 1kb, 1mb의 파일을 전송하고, 시간을 측정한다.
