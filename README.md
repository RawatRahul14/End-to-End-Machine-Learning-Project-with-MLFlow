# End-to-End-Machine-Learning-Project-with-MLFlow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?
### Steps:

Clone the repository
```bash
https://github.com/RawatRahul14/End-to-End-Machine-Learning-Project-with-MLFlow
```

### STEP 01- Create a conda environment after opening the repository
```bash
conda activate mlproj
```

### STEP 02- Install th requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now, 
```bash
open up local host and port
```



## MLflow
[Documentation](https://mlflow.org/docs/latest.index.html)

######
- mlflow ui


### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/RawatRahul14/End-to-End-Machine-Learning-Project-with-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=RawatRahul14 \
MLFLOW_TRACKING_PASSWORD=eee590c2813bb53bc8cfd269451fa6f0216df2f0 \
python script.py

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/RawatRahul14/End-to-End-Machine-Learning-Project-with-MLFlow.mlflow
export MLFLOW_TRACKING_USERNAME=###############################
export MLFLOW_TRACKING_PASSWORD=####################################
```
