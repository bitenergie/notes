# -*- coding: utf-8 -*-
"""
Introductory example - Plotting sin
===================================

This is a general example demonstrating a Matplotlib plot output, embedded
Markdown, the use of math notation and cross-linking to other examples. It would be
useful to compare the [:fontawesome-solid-download: source Python file](./plot_0_sin.py)
with the output below.

Source files for gallery examples should start with a triple-quoted header
docstring. Anything before the docstring is ignored by Mkdocs-Gallery and will
not appear in the rendered output, nor will it be executed. This docstring
requires a Markdown header, which is used as the title of the example and
to correctly build cross-referencing links.

Code and embedded Markdown text blocks follow the docstring. The first block
immediately after the docstring is deemed a code block, by default, unless you
specify it to be a text block using a line of ``#``'s or ``#%%`` (see below).
All code blocks get executed by Mkdocs-Gallery and any output, including plots
will be captured. Typically, code and text blocks are interspersed to provide
narrative explanations of what the code is doing or interpretations of code
output.

Mathematical expressions can be included as LaTeX, and will be rendered with
MathJax. See
[mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/mathjax)
for configuration of your `mkdocs.yml` as well as for syntax details. For example,
we are about to plot the following function:

$$
x \\rightarrow \\sin(x)
$$

Here the function $\sin$ is evaluated at each point the variable $x$ is defined.
When including LaTeX in a Python string, ensure that you escape the backslashes
or use a raw docstring. You do not need to do this in
text blocks (see below).
"""


# %%
from pprint import pprint

# %% [markdown]
# ## Schedule Day
# 

# %%
from schedule_day import ScheduleDay


hours = [
    1,
    1,
    1,
    1,
    1,
    1,
    0.6,
    0.4,
    0,
    0,
    0,
    0,
    0.8,
    0.4,
    0,
    0,
    0,
    0.4,
    0.8,
    0.8,
    0.8,
    1,
    1,
    1,
]
schedule = ScheduleDay(hours)
print(schedule.to_dict())
print(schedule.to_str())
print(schedule.get_sum())
print(schedule.get_len())

# %% [markdown]
# ## schedule annual
# 

# %%
from schedule_rule_annual import ScheduleRuleAnnual

schedule_annual_dict = {
    "januar": 0.8,
    "february": 0.8,
    "march": 0.8,
    "april": 0.8,
    "may": 0.8,
    "june": 0.8,
    "july": 0.8,
    "august": 0.8,
    "september": 0.8,
    "october": 0.8,
    "november": 0.8,
    "december": 0.8,
}

# test
schedule_annual = ScheduleRuleAnnual.from_dict(schedule_annual_dict)
assert schedule_annual.get_annual_simultaneity(), 0.8

schedule_annual

# %% [markdown]
# ## schedule week
# 

# %%
from schedule_rule_week import ScheduleRuleWeek

schedule_week_dict = {
    "sunday": 1,
    "monday": 1,
    "tuesday": 1,
    "wednesday": 1,
    "thursday": 1,
    "friday": 1,
    "saturday": 1,
}

schedule_week = ScheduleRuleWeek.from_dict(schedule_week_dict)


print(schedule_week)
schedule_week.get_annual_active_days()

# %% [markdown]
# ## Climate
# 

# %%
from climate import Climate

cilmate_dict = {
    "design_day_cooling": 26,
    "design_day_heating": 21,
    "average_cooling": 25,
    "average_heating": 22,
    "rel_humidity_cooling": 60,
    "rel_humidity_heating": 30,
}

climate = Climate.from_dict(cilmate_dict)
climate.to_dict()

# %% [markdown]
# ## Dimension
# 

# %%
from dimension import Dimension


dimension_dict = {
    "window_frames_factor": 0.75,
    "net_to_gross": 0.85,
    "reduction_factor_solar_heat_gain": 0.9,
    "set_solar_shading_on": 90,
    "length": 4,
    "depth": 5,
    "height": 2.5,
    "thermal_active_area": 26.5,
    "glass_percentage": 0.30,
}

dimension = Dimension.from_dict(dimension_dict)
dimension

# %% [markdown]
# ## material
# 

# %%
from materials import Material

material_dict = {
    "heat_storage_capacity": 120,
    "transmittance_glazing": 0.5,
    "transmittance_glazing_shading": 0.14,
    "light_transmittance": 0.7,
    "u_value_window": 1,
    "u_value_opaque": 0.17,
    "solar_reduction_factor": 120,
}

material = Material(**material_dict)
material_dict

# %% [markdown]
# ## Person
# 

# %%
from person import Person


person_dict = {
    "area_per_person": 35,
    "activity_level": 1.2,
    "thermal_insulation_cladding_heating": 1,
    "thermal_insulation_cladding_cooling": 0.5,
    "humidity_production_without_person": 0.5,
    "sensible_heat_output_cooling": 84,
    "sensible_heat_output_heating": 94,
    "humidity_production_heating": 51,
    "humidity_production_cooling": 66,
    "schedule_day": schedule,
    "schedule_week": schedule_week,
    "schedule_annual": schedule_annual,
}

person = Person.from_dict(person_dict)
person

# %% [markdown]
# ## Electric
# 

# %%
from electric_equipment import ElectricEquipment

el_schedule = ScheduleDay(
    [
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.8,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.8,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.8,
        1.0,
        0.2,
        0.2,
        0.2,
        0.2,
    ]
)

electric_equipment_dict = {
    "electrical_power_equipment": 10,
    "electrical_power_process": 0,
    "power_factor_outside_of_use": 0.2,
    "schedule_day": el_schedule,
    "schedule_week": schedule_week,
    "schedule_annual": schedule_annual,
}

electric_equipment = ElectricEquipment.from_dict(electric_equipment_dict)
electric_equipment

# %% [markdown]
# ## Light
# 
# - space_in = 1.27
# - space_eff = 0.70
# - pwr_area = 7.66
# - min\_ = 7.60
# - hr_ht_day = 0.74
# - cor_lintel = 1.20
# - zg_max = 0.26
# - zg = 0.18
# - hr = 550.0
# - q_ilighting = 5.65 wh/m$^2$
# - lighting_energy = 4.21
# 

# %%
from lighting import Lighting

lighting_dict = {
    "reference_illuminance": 300,
    "cor_k0": 6.0,
    "presence_type": "permanent",
    "cor_factor_simultaneity": 0.3,
    "evaluation_level": 0.75,
    "light_output_per_load": 70,
    "cor_dayligth_control": 2,
    "cor_reflexion": 1.1,
    "cor_transmission": 1,
    "cor_balcony": 1,
    "cor_sun_protection": 1.44,
    "cor_horizontal_shadow": 1,
    "maintenance_value_lighting": 0.8,
    "cor_factor_presence_control": 1,
    "schedule_day": schedule,
    "schedule_week": schedule_week,
    "schedule_annual": schedule_annual,
    "dimension": dimension,
}

light = Lighting.from_dict(lighting_dict)
print(
    f"{light.full_load_hours_annual = }\n{light.load_per_year = }\n{light.light_hours_min = }\n{light.full_load_hours = }"
)
print(light)

# %% [markdown]
# ## Ventilation
# 

# %%
from ventilation import Ventilation


ventilation_dict = {
    "schedule_day": schedule,
    "schedule_annual": schedule_annual,
    "is_mechanical": True,
    "indoor_air_category": 2,
    "outside_air_volume_flow_per_person_day": 29,
    "outside_air_volume_flow_per_person_night": 18,
    "outside_air_volume_flow_hygienic": 0.8,
    "process_air_flow": 0,
    "infiltration": 0.15,
    "controler_air_volume_flow": "single_stage",
    "temperature_heat_recovery": 0.73,
    "system_efficiency_heat_recovery": 0.7,
    "specific_fan_power": 0.56,
}

ventilation = Ventilation(**ventilation_dict)

ventilation.to_dict()



# %% [markdown]
# ## Heating
# 

# %%
from heating import Heating

heating_dict = {
    "thermal_active_min_air_flow_natural": 0.7,
    "thermal_active_min_air_exchange_rate": 0.1,
    "ventilation": ventilation,
}

heating = Heating(**heating_dict)
print(heating)



# %% [markdown]
# ## SIA 380
# 
# TO-DO:
# 
# -
# 

# %%
from energy import Sia380
import pandas as pd

sia = Sia380(dimension, climate, electric_equipment, heating, person, material, light)

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
temps = [0.4, 1.6, 5.5, 8.4, 13.4, 16.2, 18.4, 18.4, 14.0, 9.9, 4.2, 1.8]
gains_west = [22.22,34.17,55.0,64.17,79.72,84.17,90.83,81.94,60.56,39.44,20.83,16.39]
heat_bridge_factor = 1.1
elevation = 556

delta = [22 - i for i in temps]
print(f"{temps = }")
print(f"{delta = }\n")

print(f"{sia.a()= :.2f}")
print(f"{sia.time()= :.2f}")
print(f"{sia.transmission_coef_total()= :.2f}")
print(f"{sia.transmission_coef()= :.2f}")
print(f"{sia.transmission_coef_air()= :.2f}")
print(f"{sia.load_per_hour()= :.2f}")
print(f"{sia.load_per_hour_air()= :.2f}")
print(f"{sia.load_per_hour_transmission()= :.2f}")

energy = sia.energy_table(delta, days_per_month, gains_west, mechanical=True)


df_energy = pd.DataFrame(energy)
print(df_energy.sum())

df_energy = df_energy.transpose()
df_energy.to_clipboard()
df_energy.round(1)



# %%
delta = [round(25 - i, 1) for i in temps]
energy_cooling = sia.energy_table_cooling(delta, days_per_month, gains_west)

pd.DataFrame(energy_cooling).sum()


# %%
pd.DataFrame(energy_cooling)


# %%
from pprint import pprint


import matplotlib.pyplot as plt
import pandas as pd

import plotly.express as px
templates= ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
template=templates[0]

index = {
    "month": [
        "Januar",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
}

bar_colors = ["tab:red", "tab:cyan", "tab:blue", "y", "tab:orange", "tab:pink"]
df_index = pd.DataFrame(index)
df = pd.DataFrame(energy, index=index["month"])

df = df.drop(columns=["ng"])
df = df.round(2)

config = {
    "displaylogo": False,
    "modeBarButtonsToAdd": [
    ],
}

def get_month_bar(df, name):
    fig = px.bar(df, x=df.index, y=df.to_dict())

    config = {
        "displaylogo": False,
        "modeBarButtonsToAdd": [
        ],
    }
    fig.update_layout(
        {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_layout(
        xaxis_title="Monat",
        yaxis_title="kWh/m2",
        legend_font_color="white",
        font_color="white",
        title_font_color="white",
        )
        
    #fig.write_html(f"../static/plotts/{name}.html", config=config, full_html=False)
    return (fig, config)


fig, conf = get_month_bar(df,'Heating')
fig.write_html(file="../mkdocs_frontend/docs/plots/heating.html",  config=config, )
fig.show(config=conf)
fig.update_layout(template="plotly_white")
fig.write_image(file="../static/plotts/heating.svg", format="svg", )
fig.write_image(file="../mkdocs_frontend/docs/plots/heating.svg", format="svg", )

with open("../mkdocs_frontend/docs/plots/heating.json", "w") as f:
    f.write(fig.to_json())



# %%
df_c = pd.DataFrame(energy_cooling, index=index["month"])
fig, conf = get_month_bar(df_c, f"Cooling")

fig.write_html(file="../mkdocs_frontend/docs/plots/cooling.html", config=config)
fig.show(config=conf)
fig.update_layout(template="plotly_white")
fig.write_image(file="../static/plotts/cooling.svg", format="svg", )
fig.write_image(file="../mkdocs_frontend/docs/plots/cooling.svg", format="svg", )


with open("../mkdocs_frontend/docs/plots/cooling.json", "w") as f:
    f.write(fig.to_json())

print(df_c.sum())
df_energy = df_c.transpose()
df_energy.to_clipboard()
df_energy.round(1)*3.6



# %%
from moisture import CO2, MaxRelativeMoisture, RelativeMoisture


rel_moisture = 0.74  # %
moisture_total = 45
air_temperature = 5.5
mean_air_pressure = 948  # hpa
temperature = 21
rho = 1.1  # kg/m3
air_volume_flow = 20
space_volume = 50

moisture_emission = [
    48,
    48,
    48,
    48,
    48,
    48,
    33,
    25,
    10,
    10,
    10,
    10,
    40,
    25,
    10,
    10,
    10,
    25,
    40,
    40,
    40,
    48,
    48,
    48,
]


rel_mois = RelativeMoisture(
    rel_moisture,
    moisture_emission,
    air_temperature,
    mean_air_pressure,
    temperature,
    air_volume_flow,
    space_volume,
    rho,
)

print(rel_mois.relaitve_moisture)
print(rel_mois.day_one())
print(rel_mois.day_two())
print(rel_mois.day_three())
print(rel_mois.rel_humidity())


# %%
max_rel = MaxRelativeMoisture(rel_moisture, air_temperature, temperature)
print(max_rel.pv_sat_teat_si())
print(max_rel.max_relative_humidity())

# %%


import plotly.graph_objects as go
from plotly.subplots import make_subplots


df_rel = {
    "rel_hum": rel_mois.rel_humidity(),
    "max": max_rel.max_relative_humidity(),
    "Person": schedule.to_list(),
}

df = pd.DataFrame(df_rel)
# df["Airflow"] = (df['Airflow'] / df['Airflow']) * 100

def get_rel_hum_plot(name, ):
    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df.index, y=df["rel_hum"], name="Rel. Feuchte",     marker_color='lightsalmon'),
        secondary_y=False, )
    fig.add_trace(
        go.Scatter(x=df.index, y=df["max"], name="Max. Feuchte",  marker_color='red'),
        secondary_y=False, 
        )

    fig.add_trace(go.Bar(x=df.index, y=df["Person"]*100, name="Person"), 
        secondary_y=True,)

    config = {
        "displaylogo": False,
        "modeBarButtonsToAdd": [
        ],
    }
    fig.update_layout(
        {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_yaxes(title_text="Personen Profil [%]", secondary_y=True, showgrid=False)
    fig.update_layout(
        yaxis_range=[20,70],
        xaxis_title="Stunden",
        yaxis_title="Rel. Feuchte",
        template=template,
        legend_font_color="white",
        font_color="white",
        title_font_color="white",)
    
    fig.write_image(file="../mkdocs_frontend/docs/plots/rel_hum.svg", format="svg", )
    fig.write_html(file="../mkdocs_frontend/docs/plots/rel_hum.html", config=config, )
    with open("../mkdocs_frontend/docs/plots/rel_hum.json", "w") as f:
        f.write(fig.to_json())

    fig.show(config=config)

    return (fig, config)

get_rel_hum_plot("rel_hum")
df.transpose()

# %%
schedule_day = [
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.6,
    0.4,
    0.0,
    0.0,
    0.0,
    0.0,
    0.8,
    0.4,
    0.0,
    0.0,
    0.0,
    0.4,
    0.8,
    0.8,
    0.8,
    1.0,
    1.0,
    1.0,
]

co2 = CO2(
    schedule_day,
    net_floor_area=20,
    space_volume=50,
    air_volume_flow=0.98,
    person_per_area=35,
    person_activity=1.2,
)
print(f"{co2.co2_per_hour() =   } l/Person*h")
print(f"{co2.volume_flow()  =   } m3")
print(f"{co2.day_one()      =   } ppm")
print(f"{co2.day_two()      =   } ppm")
print(f"{co2.day_three()    =   } ppm")

# %%
import plotly.graph_objects as go
from plotly.subplots import make_subplots
df_co2 = {
    "Person profile": co2.schedule_day,
    "Airflow": co2.volume_flow(),
    "co2": co2.day_three(),
}

df = pd.DataFrame(df_co2)
df["Airflow"] = (df['Airflow'] / df['Airflow']) * 100

def get_co2_plot(name, ):
    fig = go.Figure()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(x=df.index, y=df["Person profile"]*100, name="Person",     marker_color='lightsalmon'),
        secondary_y=False, )
    fig.add_trace(
        go.Bar(x=df.index, y=df["Airflow"], name="Airflow",  marker_color='LightSkyBlue'),
        secondary_y=False, 
        )

    fig.add_trace(go.Scatter(x=df.index, y=df.co2, name="CO2"), 
        secondary_y=True,)

    config = {
        "displaylogo": False,
        "modeBarButtonsToAdd": [
        ],
    }
    fig.update_layout(
        {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_yaxes(title_text="ppm", secondary_y=True, showgrid=False)
    fig.update_layout(
        xaxis_title="Stunden",
        yaxis_title="%",
        template=template,
        legend_font_color="white",
        font_color="white",
        title_font_color="white",)
    
    #fig.write_html(file="../mkdocs_frontend/docs/plots/{name}.html", config=config)
    fig.write_image(file="../mkdocs_frontend/docs/plots/co_2.svg", format="svg", )
    fig.write_html(file="../mkdocs_frontend/docs/plots/co_2.html", config=config, )
    with open("../mkdocs_frontend/docs/plots/co_2.json", "w") as f:
        f.write(fig.to_json())

    fig.show(config=config)

    return (fig, config)

get_co2_plot("co_2")
df.transpose()

# %% [markdown]
# ## design day august
# 

# %%
from design_day import DesignDay

solar = [
    0,
    0,
    0,
    0,
    3,
    32,
    65,
    77,
    97,
    112,
    117,
    128,
    267,
    456,
    602,
    680,
    670,
    551,
    238,
    0,
    0,
    0,
    0,
    0,
]
temp = [
    19.9,
    19.3,
    18.8,
    18.4,
    18.3,
    18.9,
    20.3,
    21.9,
    24.0,
    25.0,
    26.7,
    28.2,
    29.6,
    30.5,
    31.4,
    31.9,
    32.0,
    30.6,
    27.4,
    26.4,
    26.9,
    24.9,
    22.9,
    21.8,
]
rel = [
    84,
    85,
    85,
    88,
    87,
    87,
    81,
    75,
    66,
    63,
    57,
    54,
    50,
    47,
    42,
    34,
    34,
    42,
    58,
    47,
    39,
    45,
    52,
    61,
]

dd = DesignDay(
    solar,
    temp,
    rel,
    dimension,
    electric_equipment,
    person,
    material,
    heating,
    light,
    climate,
    ventilation,
)
print(dd.beleuchtung_sommer())
print(dd.solar)
print(dd.day_light_without_shading())
print(dd.day_light_with_shading())
dd.lightning_load()
print(f"{dd.delta_temperature()    =   }\n")
print(f"{dd.solar_load()            =   }\n")
print(f"{dd.lightning_load()            =   }\n")
print(f"{dd.person_load()            =   }\n")
print(f"{dd.equipment_load()            =   }\n")
print(f"{dd.transmission_load()    =   }\n")
print(f"{dd.ventilation_load()     =   }\n")
print(f"{dd.cooling_load()          =   }\n")

# %%
df = pd.DataFrame(dd.get_load_table())


def get_month_bar(df, name, text=False):
    fig = px.bar(df, x=df.index, y=df.to_dict(),  text_auto=text,)
    fig.update_layout(
        {
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        }
    )
    fig.update_layout(
        template=template,
        xaxis_title="Stunden",
        yaxis_title="kW/m2",
        legend_font_color="white",
        font_color="white",
        title_font_color="white",)
    config = {
        "displaylogo": False,
        "modeBarButtonsToAdd": [
        ],
    }
    fig.show(config=config)
    fig.write_html(f"../static/plotts/{name}.html", config=config, full_html=False)
    fig.write_image(file="../static/plotts/ddy_august.svg", format="svg")
    fig.write_image(file="../mkdocs_frontend/docs/plots/ddy_august.svg", format="svg", )
    fig.write_html(file="../mkdocs_frontend/docs/plots/ddy_august.html", config=config, )

    with open("../mkdocs_frontend/docs/plots/ddy_august.json", "w") as f:
        f.write(fig.to_json())


get_month_bar(df, "Design Day August", False)
print(df.min())
df.transpose()



# %%
import plotly.graph_objects as go
animals=['Fenster Tag / Nacht', 'Fenster nur bei benutzung', 'keine Fenster']

fig = go.Figure(data=[
    go.Bar(name='nicht Notwendig', x=animals, y=[140, 100, 80]),
    go.Bar(name='Erwünscht', x=animals, y=[60, 40, 40]),
    go.Bar(name='Notwendig', x=animals, y=[10, 70, 90]),
    go.Scatter(name="Wattstunden pro Tag",x=animals, y=[117,117,117], marker_color='white')
])
fig.update_layout(
    {
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    }
)
fig.update_layout(
    template=template,
    xaxis_title="Art der Belüftung",
    yaxis_title="Wh/m2*day",
    legend_font_color="white",
    font_color="white",
    title_font_color="white",)
config = {
    "displaylogo": False,
    "modeBarButtonsToAdd": [
    ],
}
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
fig.write_html(file="../mkdocs_frontend/docs/plots/is_cooling.html", config=config, )


# %% [markdown]
# ## Model 
# 

# %%
from sia_base_model import Model

model_lite = {
    "identifier": "test_lite",
    "dimension": {
        "window_frames_factor": 0.75,
        "net_to_gross": 0.85,
        "reduction_factor_solar_heat_gain": 0.9,
        "set_solar_shading_on": 90,
        "length": 4,
        "depth": 5,
        "height": 2.5,
        "thermal_active_area": 26.5,
        "glass_percentage": 0.3,
    },
    "material": {
        "heat_storage_capacity": 120,
        "transmittance_glazing": 0.5,
        "transmittance_glazing_shading": 0.14,
        "light_transmittance": 0.7,
        "u_value_window": 1,
        "u_value_opaque": 0.17,
        "solar_reduction_factor": 120,
    },
    "climate": {
        "design_day_cooling": 26,
        "design_day_heating": 21,
        "average_cooling": 25,
        "average_heating": 22,
        "rel_humidity_cooling": 60,
        "rel_humidity_heating": 30,
        "average_air_speed_cooling": 0.18,
        "average_air_speed_heating": 0.13,
    },
    "person": {
        "area_per_person": 35,
        "activity_level": 1.2,
        "thermal_insulation_cladding_heating": 1,
        "thermal_insulation_cladding_cooling": 0.5,
        "humidity_production_without_person": 0.5,
        "sensible_heat_output_cooling": 84,
        "sensible_heat_output_heating": 94,
        "humidity_production_heating": 51,
        "humidity_production_cooling": 66,
    },
    "electric_equipment": {
        "electrical_power_equipment": 10,
        "electrical_power_process": 0,
        "power_factor_outside_of_use": 0.2,
    },
    "lighting": {
        "reference_illuminance": 300,
        "cor_k0": 6.0,
        "presence_type": "permanent",
        "cor_factor_simultaneity": 0.3,
        "evaluation_level": 0.75,
        "light_output_per_load": 70,
        "cor_dayligth_control": 2,
        "cor_reflexion": 1.1,
        "cor_transmission": 1,
        "cor_balcony": 1,
        "cor_sun_protection": 1.44,
        "cor_horizontal_shadow": 1,
        "maintenance_value_lighting": 0.8,
        "cor_factor_presence_control": 1,
    },
    "ventilation": {
        "is_mechanical": False,
        "indoor_air_category": 2,
        "outside_air_volume_flow_per_person_day": 29,
        "outside_air_volume_flow_per_person_night": 18,
        "outside_air_volume_flow_hygienic": 0.8,
        "process_air_flow": 0,
        "infiltration": 0.15,
        "controler_air_volume_flow": "single_stage",
        "temperature_heat_recovery": 0.73,
        "system_efficiency_heat_recovery": 0.7,
        "specific_fan_power": 0.56,
    },
    "water": {
        "reference_unit": "person",
        "hot_per_unit": 35,
        "person_per_unit": 1,
        "hot_to_cold_factor": 4,
    },
    "schedule_rule_annual": {
        "januar": 0.8,
        "february": 0.8,
        "march": 0.8,
        "april": 0.8,
        "may": 0.8,
        "june": 0.8,
        "july": 0.8,
        "august": 0.8,
        "september": 0.8,
        "october": 0.8,
        "november": 0.8,
        "december": 0.8,
    },
    "schedule_rule_week": {
        "monday": 1,
        "tuesday": 1,
        "wednesday": 1,
        "thursday": 1,
        "friday": 1,
        "saturday": 1,
        "sunday": 1,
    },
    "schedule_day": {
        "hours": [
            1,
            1,
            1,
            1,
            1,
            1,
            0.6,
            0.4,
            0,
            0,
            0,
            0,
            0.8,
            0.4,
            0,
            0,
            0,
            0.4,
            0.8,
            0.8,
            0.8,
            1,
            1,
            1,
        ]
    },
    "schedule_day_electric": {
        "hours": [
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.8,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.8,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.8,
            1.0,
            0.2,
            0.2,
            0.2,
            0.2,
        ]
    },
    "heating": {
        "thermal_active_min_air_flow_natural": 0.7,
        "thermal_active_min_air_exchange_rate": 0.1,
    },
    "acoustics": {
        "noise_sensitivity": "normal",
        "single_functional_noises": 33,
        "single_user_noises": 38,
        "continues_hvac_equipment_noise": 28,
    },
    "cooling": {
        "external_heat_input_performance": 0,
        "internal_heat_inputs": 0,
        "internal_heat_inputs_per_day": 0,
        "climate_power_requirements": 0,
        "annual_full_load_hours": 0,
        "annual_air_conditioning_refrigeration_requirement": 0,
    },
}

base_model_lite = Model.from_small_dict(model_lite)
base_model_lite.to_dict()

# %%
import json
from sia_base_model import Model

acoustics = {
        "noise_sensitivity": "normal",
        "single_functional_noises": 33,
        "single_user_noises": 38,
        "continues_hvac_equipment_noise": 28,
}

water_dict = {
    "reference_unit": "person",
    "hot_per_unit": 35,
    "person_per_unit": 1,
    "hot_to_cold_factor": 4,
    "person": person,
    "schedule_week": schedule_week,
    "schedule_annual": schedule_annual,
  }

cooling_dict = {
  "external_heat_input_performance": 0,
  "internal_heat_inputs": 0,
  "internal_heat_inputs_per_day": 0,
  "climate_power_requirements": 0,
  "annual_full_load_hours": 0,
  "annual_air_conditioning_refrigeration_requirement": 0
}

model_dict = {
    "identifier": "default", 
    "schedule_day": {"hours": hours},
    "schedule_rule_annual": schedule_annual_dict,
    "schedule_rule_week": schedule_week_dict,
    "climate": cilmate_dict,
    "dimension": dimension_dict,
    "acoustics": acoustics,
    "material": material_dict,
    "person": person_dict,
    "electric_equipment": electric_equipment_dict,
    "lighting": lighting_dict,
    "ventilation": ventilation_dict,
    "heating": heating_dict,
    "water": water_dict,
    "cooling": cooling_dict,
}

base_model = Model.from_dict(model_dict)

m = base_model.to_dict()
model_dict

# %%


with open("../mkdocs_frontend/docs/data.json", "w") as file:
    json.dump(obj=m, fp=file, sort_keys=True,  indent=2, ensure_ascii=False)


import chevron

with open('../mkdocs_frontend/docs/template.md', 'r') as f:
    generated_md = chevron.render(f, m)
with open('../mkdocs_frontend/docs/generated.md', 'w') as f:
    f.write(generated_md)

print(generated_md)

#json.dumps(m, sort_keys=True,  indent=2, ensure_ascii=False)


# %%
# pprint(model_dict)
print(json.dumps(m, sort_keys=True,  indent=2, ensure_ascii=False))



# %%

import urllib, requests

openapi_json = urllib.request.urlretrieve("http://localhost:8000/openapi.json", "../tmp/openapi.json")
print(openapi_json)




# %%
pprint(model_dict)



# %%


with open("../tmp/openapi.json", "r") as f:
    openapi = json.load(f)
inputs={}
req_obj = ['Acoustics', 'Climate', 'Cooling', 'Dimension', 'ElectricEquipment', 'HTTPValidationError', 'Heating', 'Lighting', 'Material', 'ModelName', 'Person', 'ScheduleDay', 'ScheduleRuleAnnual', 'ScheduleRuleWeek', 'Model', 'SpaceType', 'Ventilation', 'Water']
comp_keys = openapi["components"]["schemas"].keys()
for i in comp_keys:
    if i in req_obj:
        for k,j in openapi["components"]["schemas"][i].items():
            if k == "required":
                #print(i, "=", j)
                #print(f'<option value="{i}">{i}</option>')
                inputs[i] = j
inputs

print(json.dumps(inputs, sort_keys=True,  indent=2, ensure_ascii=False))




