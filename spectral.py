import streamlit as st

def spectral_terms(terms):
    # Function to process spectral terms
    result = []
    for term in terms:
        result.append(f"Spectral Term: {term}")
    return result

def main():
    st.title("Spectral Terms Calculator")
    
    # User input for spectral terms
    terms_input = st.text_input("Enter spectral terms separated by commas (e.g., term1, term2, term3):")
    
    if st.button("Calculate"):
        terms = [term.strip() for term in terms_input.split(",")]
        result = spectral_terms(terms)
        st.write("## Results")
        for term in result:
            st.write(term)

if __name__ == "__main__":
    main()
