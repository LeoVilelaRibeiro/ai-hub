run-dev:
	poetry run streamlit run src/ai-hub/streamlit_app.py --server.port=8501 --server.runOnSave=true

code-check:
	poetry run pre-commit run --all-files
