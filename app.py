import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(
    page_title="Wine Quality Classifier",
    page_icon="🍷",
    layout="centered"
)

def apply_log(x):
  return np.log1p(x)

def apply_power_transform(x):
  return x**2

@st.cache_resource
def load_model(model_path):
    """Function to load the trained model."""
    try:
        with open(model_path, 'rb') as file:
            model = joblib.load(file)
        return model
    except FileNotFoundError:
        st.error(f"Model file not found at: {model_path}")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

def user_interface():
    """Creates the user interface to collect the wine's characteristics."""
    st.sidebar.header("Enter Wine Characteristics")
    
    # Dictionary to easily create the sliders
    # IMPORTANT: The dictionary keys must be EXACTLY the same as the
    #            column names used to train your model.
    parameters = {
        'fixed_acidity': st.sidebar.slider('Fixed Acidity (g/dm³)', 4.0, 16.0, 7.4),
        'volatile_acidity': st.sidebar.slider('Volatile Acidity (g/dm³)', 0.1, 1.6, 0.7),
        'citric_acid': st.sidebar.slider('Citric Acid (g/dm³)', 0.0, 1.0, 0.0),
        'chlorides': st.sidebar.slider('Chlorides (g/dm³)', 0.01, 0.62, 0.076),
        'free_sulfur_dioxide': st.sidebar.slider('Free Sulfur Dioxide (mg/dm³)', 1, 72, 11),
        'total_sulfur_dioxide': st.sidebar.slider('Total Sulfur Dioxide (mg/dm³)', 6, 289, 34),
        'density': st.sidebar.slider('Density (g/cm³)', 0.990, 1.004, 0.997),
        'sulphates': st.sidebar.slider('Sulphates (g/dm³)', 0.3, 2.0, 0.56),
        'alcohol': st.sidebar.slider('Alcohol (% vol.)', 8.0, 15.0, 9.4)
    }
    
    data_df = pd.DataFrame(parameters, index=[0])
    return data_df

def main():
    """Main function that runs the Streamlit application."""
    st.title("🍷 Wine Quality Classifier")
    st.markdown("""
    This app uses a Machine Learning model to predict whether a wine is of **good** or **bad** quality
    based on its physicochemical characteristics.
    
    Adjust the parameters on the sidebar and click **"Check Quality"**.
    """)

    model = load_model('wine_model.joblib')
    
    if model:
        user_data_df = user_interface()

        st.subheader("Selected Wine Characteristics:")
        st.dataframe(user_data_df, use_container_width=True)

        if st.sidebar.button("Check Quality"):
            model_input_df = user_data_df.copy()

            # Calculate the sulfur ratio, handling division by zero
            if model_input_df['total_sulfur_dioxide'][0] > 0:
                sulfur_ratio = model_input_df['free_sulfur_dioxide'][0] / model_input_df['total_sulfur_dioxide'][0]
            else:
                sulfur_ratio = 0
            model_input_df['sulfur_ratio'] = sulfur_ratio
           
            # Citric acid is a binary feature in the model
            model_input_df['has_citric_acid'] = (model_input_df['citric_acid'] > 0).astype(int)
            
            columns_to_drop = ['free_sulfur_dioxide', 'total_sulfur_dioxide', 'citric_acid']
            model_input_df = model_input_df.drop(columns=columns_to_drop)

            prediction = model.predict(model_input_df)

            st.subheader("Analysis Result")
            
            if prediction[0] == 1:
                st.success("This wine is of **GOOD** quality! 🎉", icon="✔️")
            else:
                st.error("This wine is of **BAD** quality. 😢", icon="✖️")

if __name__ == '__main__':
    main()
