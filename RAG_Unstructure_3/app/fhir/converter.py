def to_fhir(text):
    return {
        "resourceType": "Patient",
        "summary": text[:500]
    }