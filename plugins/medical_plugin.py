import os
from semantic_kernel.functions import kernel_function
from semantic_kernel import kernel


class MedicalPlugin:
    @kernel_function(name="diagnose_condition", description="Diagnoses a health condition based on symptoms")
    def diagnose_condition(self, symptoms: str, language: str) -> str:
        """Diagnoses a medical condition based on the symptoms provided by the user."""
        prompt_file = "prompts/diagnosis.txt"
        if language == "es":
            prompt_file = "prompts/diagnosis_es.txt"  # Spanish version if needed
        return self._get_prompt_response(symptoms, prompt_file)

    @kernel_function(name="recommend_medicine", description="Recommends medicine based on symptoms")
    def recommend_medicine(self, symptoms: str, language: str) -> str:
        """Recommends medicine based on symptoms."""
        prompt_file = "prompts/medicine.txt"
        if language == "es":
            prompt_file = "prompts/medicine_es.txt"  # Spanish version if needed
        return self._get_prompt_response(symptoms, prompt_file)

    @kernel_function(name="suggest_remedy", description="Suggests a home remedy based on symptoms")
    def suggest_remedy(self, symptoms: str, language: str) -> str:
        """Suggests a home remedy based on symptoms."""
        prompt_file = "prompts/remedy.txt"
        if language == "es":
            prompt_file = "prompts/remedy_es.txt"  # Spanish version if needed
        return self._get_prompt_response(symptoms, prompt_file)

    @kernel_function(name="prevent_illness", description="Provides preventive tips for health conditions")
    def prevent_illness(self, symptoms: str, language: str) -> str:
        """Provides preventive tips for health conditions."""
        prompt_file = "prompts/prevention.txt"
        if language == "es":
            prompt_file = "prompts/prevention_es.txt"  # Spanish version if needed
        return self._get_prompt_response(symptoms, prompt_file)

    def _get_prompt_response(self, symptoms: str, prompt_file: str) -> str:
        """Reads the prompt file and generates a response."""
        try:
            with open(prompt_file, "r") as f:
                prompt_content = f.read()
            # Replace the placeholder in the prompt with the symptoms
            prompt_content = prompt_content.replace("{{symptoms}}", symptoms)
            # Here you would integrate with the kernel API or AI service
            return prompt_content  # Adjusted to return the processed content
        except FileNotFoundError:
            return f"Error: The prompt file {prompt_file} was not found."
        except Exception as e:
            return f"Error: {str(e)}"
