# app/schemas.py
from pydantic import BaseModel, Field


class StudentInputSchema(BaseModel):
    marital_status: int = Field(..., alias="Marital status")  # lowercase s
    application_mode: int = Field(..., alias="Application mode")
    application_order: int = Field(..., alias="Application order")
    course: int = Field(..., alias="Course")
    # trailing tab
    daytime_evening_attendance: int = Field(...,
                                            alias="Daytime/evening attendance\t")
    previous_qualification: int = Field(..., alias="Previous qualification")
    previous_qualification_grade: float = Field(
        ..., alias="Previous qualification (grade)")
    nationality: int = Field(..., alias="Nacionality")
    mother_qualification: int = Field(..., alias="Mother's qualification")
    father_qualification: int = Field(..., alias="Father's qualification")
    mother_occupation: int = Field(..., alias="Mother's occupation")
    father_occupation: int = Field(..., alias="Father's occupation")
    admission_grade: float = Field(..., alias="Admission grade")
    displaced: int = Field(..., alias="Displaced")
    educational_special_needs: int = Field(...,
                                           alias="Educational special needs")
    debtor: int = Field(..., alias="Debtor")
    tuition_fees_up_to_date: int = Field(..., alias="Tuition fees up to date")
    gender: int = Field(..., alias="Gender")
    scholarship_holder: int = Field(..., alias="Scholarship holder")
    age_at_enrollment: int = Field(..., alias="Age at enrollment")
    international: int = Field(..., alias="International")
    curricular_units_1st_sem_credited: int = Field(
        ..., alias="Curricular units 1st sem (credited)")
    curricular_units_1st_sem_enrolled: int = Field(
        ..., alias="Curricular units 1st sem (enrolled)")
    curricular_units_1st_sem_evaluations: int = Field(
        ..., alias="Curricular units 1st sem (evaluations)")
    curricular_units_1st_sem_approved: int = Field(
        ..., alias="Curricular units 1st sem (approved)")
    curricular_units_1st_sem_grade: float = Field(
        ..., alias="Curricular units 1st sem (grade)")
    curricular_units_1st_sem_without_evaluations: int = Field(
        ..., alias="Curricular units 1st sem (without evaluations)")
    curricular_units_2nd_sem_credited: int = Field(
        ..., alias="Curricular units 2nd sem (credited)")
    curricular_units_2nd_sem_enrolled: int = Field(
        ..., alias="Curricular units 2nd sem (enrolled)")
    curricular_units_2nd_sem_evaluations: int = Field(
        ..., alias="Curricular units 2nd sem (evaluations)")
    curricular_units_2nd_sem_approved: int = Field(
        ..., alias="Curricular units 2nd sem (approved)")
    curricular_units_2nd_sem_grade: float = Field(
        ..., alias="Curricular units 2nd sem (grade)")
    curricular_units_2nd_sem_without_evaluations: int = Field(
        ..., alias="Curricular units 2nd sem (without evaluations)")
    unemployment_rate: float = Field(..., alias="Unemployment rate")
    inflation_rate: float = Field(..., alias="Inflation rate")
    gdp: float = Field(..., alias="GDP")

    model_config = {"populate_by_name": True}
