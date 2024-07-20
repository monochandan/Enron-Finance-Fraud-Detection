# ML model deployment in docker : Financial Fraud Detection

- scikit-learn==1.5.0
- nltk==3.8.1
- flask==3.0.3 
- flask-cors==4.0.1
- python==3.10

# Build an image (Dockerize) and run on Docker container:

## Use VS code

## Downloade project (git bash):
    
    git clone https://github.com/monochandan/tweet-sentiment-docker-ML-Model.git // clone the repository in the local computer

## Open in VS code

    cd api // rediect to api directory (in VS code terminal)

    docker compose up --build // build the image in local computer (in VS code git bash terminal)

  ## Then in browser:

      http://localhost:500




# Directly run on Docker without building an image locally:


## Run in command prompt or powershell:

    docker run -p5000:5000 chandanmonotosh554/mlapp

## Then in browser:

      http://localhost:500

<img width="333" alt="image" src="https://github.com/user-attachments/assets/7835132b-757e-44c2-a285-40f8257052c5">
