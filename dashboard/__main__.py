import altair as alt
import pandas as pd
import streamlit as st

from jer_cdm.concepts import Ontology
from jer_cdm.measurement import add_measurement_row, get_measurement_data


@st.cache
def measurement_data():
    return get_measurement_data()


def make_dashboard():
    measurement_df = measurement_data()
    ontology = Ontology()

    renaming = {c: ontology.get_concept_name_from_id(
        c) for c in measurement_df.measurement_concept_id.unique()
    }
    visualization_df = measurement_df.copy()
    unit = ontology.get_concept_name(
        ontology.get_concept_from_id(
            measurement_df['unit_concept_id'].iloc[0]
        )
    )
    visualization_df["measurement_concept_name"] = \
        measurement_df.measurement_concept_id.replace(renaming)

    visualization_df = visualization_df[
        ['datetime', 'value', 'measurement_concept_name']]
    # visualization_df['observation_date'] = pd.to_datetime(
    #     visualization_df['observation_date'])
    # pd_unit = unit[0].upper()
    # time_value = pd.to_timedelta(
    #     visualization_df['value_as_number'], unit=pd_unit)
    # visualization_df['value'] = time_value / pd.Timedelta('1 hour')
    # visualization_df['minutes'] = (
    #     (time_value
    #      / pd.Timedelta('1 minute')).astype(int)
    #     % 60
    # ).astype(str)
    # visualization_df['hours'] = (
    #     (time_value
    #      / pd.Timedelta('1 hour')).astype(int)
    # ).astype(str)
    visualization_df['description'] = (
        + visualization_df['value'].astype(str) + ' '
        + unit + ' '
        # + visualization_df['measurement_concept_name'].astype(str)
        + ' '
        + visualization_df['datetime'].astype(str)
        + ' '
    )

    width = min(len(visualization_df) * 10, 800)
    single_nearest = alt.selection_single(on='mouseover', nearest=True)
    chart = alt.Chart(visualization_df).mark_point().encode(
        x='datetime',
        y='value',
        # color='observation_concept_name',
        tooltip='description'
    ).add_selection(single_nearest).interactive().properties(
        width=width,
    )
    st.altair_chart(chart)
    st.title("Source Data")
    st.write(measurement_df)


if __name__ == '__main__':
    make_dashboard()
