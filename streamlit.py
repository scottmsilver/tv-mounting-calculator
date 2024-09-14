import math
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go

def calculate_tv_height(viewing_distance, eye_height, tv_size, scenario, fov):
    viewing_distance_inches = viewing_distance * 12
    tv_width, tv_height = tv_size * 0.87, tv_size * 0.49
    optimal_angle = math.radians(fov / 2)  # Use half of FOV as the optimal angle
    tv_center_height = eye_height + (viewing_distance_inches * math.tan(optimal_angle))
    return {
        "tv_width": tv_width, "tv_height": tv_height,
        "tv_center_height": tv_center_height,
        "mounting_height": tv_center_height + (tv_height / 2),
        "optimal_angle_degrees": math.degrees(optimal_angle),
        "eye_height": eye_height,
        "eye_distance": viewing_distance_inches
    }

def calculate_ideal_tv_size(viewing_distance, fov):
    return round(viewing_distance * 12 * math.tan(math.radians(fov/2)) * 2 / 0.87)

def create_room(fig, viewing_distance, room_width):
    fig.add_trace(go.Mesh3d(
        x=[0, viewing_distance*12, viewing_distance*12, 0, 0, viewing_distance*12, viewing_distance*12, 0],
        y=[-room_width/2, -room_width/2, room_width/2, room_width/2, -room_width/2, -room_width/2, room_width/2, room_width/2],
        z=[0, 0, 0, 0, 120, 120, 120, 120],
        i=[0, 0, 0, 1, 4],
        j=[1, 2, 4, 2, 5],
        k=[2, 3, 7, 3, 6],
        opacity=0.2,
        color='lightblue'
    ))

def create_furniture(fig, scenario, furniture_depth, furniture_width, furniture_height, furniture_color):
    if scenario == "living_room":
        couch_back_height = 36
        couch_seat_height = 18
        fig.add_trace(go.Mesh3d(
            x=[0, furniture_depth, furniture_depth, 0, 0, furniture_depth, furniture_depth, 0],
            y=[-furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2, -furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2],
            z=[0, 0, 0, 0, couch_seat_height, couch_seat_height, couch_seat_height, couch_seat_height],
            color=furniture_color,
            opacity=0.8
        ))
        fig.add_trace(go.Mesh3d(
            x=[0, furniture_depth, furniture_depth, 0, 0, furniture_depth, furniture_depth, 0],
            y=[-furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2, -furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2],
            z=[couch_seat_height, couch_seat_height, couch_seat_height, couch_seat_height, couch_back_height, couch_back_height, couch_back_height, couch_back_height],
            color=furniture_color,
            opacity=0.8
        ))
    else:
        fig.add_trace(go.Mesh3d(
            x=[0, furniture_depth, furniture_depth, 0, 0, furniture_depth, furniture_depth, 0],
            y=[-furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2, -furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2],
            z=[0, 0, 0, 0, furniture_height, furniture_height, furniture_height, furniture_height],
            color=furniture_color,
            opacity=0.8
        ))
        fig.add_trace(go.Mesh3d(
            x=[0, furniture_depth, furniture_depth, 0, 0, furniture_depth, furniture_depth, 0],
            y=[-furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2, -furniture_width/2, -furniture_width/2, furniture_width/2, furniture_width/2],
            z=[furniture_height, furniture_height, furniture_height, furniture_height, furniture_height+10, furniture_height+10, furniture_height+10, furniture_height+10],
            color=furniture_color,
            opacity=0.8
        ))

def create_person(fig, scenario, person_x, person_y, person_z, eye_height):
    if scenario == "living_room":
        torso_height = 20
        head_height = 10
        leg_length = 15
        arm_length = 10

        fig.add_trace(go.Mesh3d(
            x=[person_x, person_x, person_x, person_x],
            y=[person_y - 5, person_y + 5, person_y + 5, person_y - 5],
            z=[person_z, person_z, person_z + torso_height, person_z + torso_height],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x, person_x, person_x, person_x],
            y=[person_y - 3, person_y + 3, person_y + 3, person_y - 3],
            z=[person_z + torso_height, person_z + torso_height, person_z + torso_height + head_height, person_z + torso_height + head_height],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x - 2, person_x + 2, person_x + 2, person_x - 2],
            y=[person_y - 2, person_y - 2, person_y + 2, person_y + 2],
            z=[person_z - leg_length, person_z - leg_length, person_z, person_z],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x - arm_length, person_x + arm_length, person_x + arm_length, person_x - arm_length],
            y=[person_y - 1, person_y - 1, person_y + 1, person_y + 1],
            z=[person_z + torso_height / 2, person_z + torso_height / 2, person_z + torso_height / 2, person_z + torso_height / 2],
            i=[0, 0],
            j=[1, 2],
            k=[2, 3],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Scatter3d(
            x=[person_x], y=[person_y], z=[eye_height],
            mode='markers',
            marker=dict(size=5, color='blue'),
            name='Eyes'
        ))
    else:
        torso_length = 36
        head_length = 10
        leg_length = 15
        arm_length = 10

        fig.add_trace(go.Mesh3d(
            x=[person_x, person_x + torso_length, person_x + torso_length, person_x],
            y=[person_y - 5, person_y - 5, person_y + 5, person_y + 5],
            z=[person_z, person_z, person_z, person_z],
            i=[0],
            j=[1],
            k=[2],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x, person_x + head_length, person_x + head_length, person_x],
            y=[person_y - 3, person_y - 3, person_y + 3, person_y + 3],
            z=[person_z, person_z, person_z, person_z],
            i=[0],
            j=[1],
            k=[2],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x + torso_length, person_x + torso_length + leg_length, person_x + torso_length + leg_length, person_x + torso_length],
            y=[person_y - 2, person_y - 2, person_y + 2, person_y + 2],
            z=[person_z, person_z, person_z, person_z],
            i=[0],
            j=[1],
            k=[2],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Mesh3d(
            x=[person_x + torso_length / 2 - arm_length, person_x + torso_length / 2 + arm_length, person_x + torso_length / 2 + arm_length, person_x + torso_length / 2 - arm_length],
            y=[person_y - 1, person_y - 1, person_y + 1, person_y + 1],
            z=[person_z, person_z, person_z, person_z],
            i=[0],
            j=[1],
            k=[2],
            color='blue',
            opacity=0.8
        ))

        fig.add_trace(go.Scatter3d(
            x=[person_x + head_length / 2], y=[person_y], z=[person_z],
            mode='markers',
            marker=dict(size=5, color='blue'),
            name='Eyes'
        ))

def create_tv(fig, result, viewing_distance):
    tv_bottom = result['tv_center_height'] - result['tv_height'] / 2
    tv_top = result['tv_center_height'] + result['tv_height'] / 2
    tv_x = viewing_distance * 12
    fig.add_trace(go.Mesh3d(
        x=[tv_x, tv_x, tv_x, tv_x],
        y=[-result['tv_width']/2, result['tv_width']/2, result['tv_width']/2, -result['tv_width']/2],
        z=[tv_bottom, tv_bottom, tv_top, tv_top],
        i=[0, 0],
        j=[1, 2],
        k=[2, 3],
        color='black',
        opacity=0.8
    ))

def create_viewing_angle(fig, eye_x, tv_x, eye_height, tv_center_height):
    fig.add_trace(go.Scatter3d(
        x=[eye_x, tv_x],
        y=[0, 0],
        z=[eye_height, tv_center_height],
        mode='lines',
        line=dict(color='red', width=5, dash='dash'),
        showlegend=False
    ))

def create_annotations(fig, result, viewing_distance, furniture_depth, eye_height, furniture_name, furniture_height):
    tv_x = viewing_distance * 12
    tv_bottom = result['tv_center_height'] - result['tv_height'] / 2
    tv_top = result['tv_center_height'] + result['tv_height'] / 2
    fig.add_trace(go.Scatter3d(
        x=[5, tv_x+5, viewing_distance*6, furniture_depth+5, tv_x+5, tv_x+5, tv_x+5],
        y=[0, 0, 0, 0, 0, result['tv_width']/2+5, 0],
        z=[eye_height, result['tv_center_height'], 10, furniture_height/2, tv_bottom, result['tv_center_height'], tv_top],
        mode='text',
        text=[f"Eye Height: {eye_height:.1f}\"", f"TV Center: {result['tv_center_height']:.1f}\"",
              f"Viewing Distance: {viewing_distance:.1f} ft", f"{furniture_name} Height: {furniture_height}\"",
              f"TV Bottom: {tv_bottom:.1f}\"", f"TV Width: {result['tv_width']:.1f}\"", f"TV Top: {tv_top:.1f}\""],
        textposition="top center"
    ))

def create_setup_plot_3d(viewing_distance, eye_height, tv_size, scenario, fov):
    result = calculate_tv_height(viewing_distance, eye_height, tv_size, scenario, fov)
    
    furniture = {
        "living_room": ("Couch", 86, 36, 36, "brown"),
        "bedroom": ("Bed", 76, 24, 80, "gray")
    }
    furniture_name, furniture_width, furniture_height, furniture_depth, furniture_color = furniture[scenario]
    
    fig = go.Figure()
    
    room_width = max(furniture_width, result['tv_width']) + 20
    create_room(fig, viewing_distance, room_width)
    create_furniture(fig, scenario, furniture_depth, furniture_width, furniture_height, furniture_color)
    
    if scenario == "living_room":
        person_x = furniture_depth / 2
        person_y = 0
        person_z = 18
    else:
        person_x = 5
        person_y = 0
        person_z = furniture_height
    
    create_person(fig, scenario, person_x, person_y, person_z, eye_height)
    create_tv(fig, result, viewing_distance)
    
    eye_x = furniture_depth/2 if scenario == "living_room" else person_x + 5
    create_viewing_angle(fig, eye_x, viewing_distance * 12, eye_height, result['tv_center_height'])
    create_annotations(fig, result, viewing_distance, furniture_depth, eye_height, furniture_name, furniture_height)
    
    fig.update_layout(
        scene = dict(
            xaxis = dict(nticks=4, range=[0, viewing_distance*12+10],),
            yaxis = dict(nticks=4, range=[-room_width/2-10, room_width/2+10],),
            zaxis = dict(nticks=4, range=[0, 120],),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.5)
        ),
        width=800,
        height=600,
        title=f"3D TV Mounting Setup - {scenario.capitalize()} (FOV: {fov}°)",
        showlegend=False
    )
    
    return fig

def main():
    st.set_page_config(layout="wide")
    st.title("3D TV Mounting Height Calculator")

    col1, col2 = st.columns([1, 3])

    with col1:
        scenario = st.selectbox("Select scenario", ["living_room", "bedroom"])
        viewing_distance = st.slider("Viewing distance (feet)", 5, 20, 10)
        eye_height = st.slider("Eye height (inches)", 20, 60, 42 if scenario == "living_room" else 30)
        
        fov_option = st.radio("Choose Field of View (FOV):", ["THX (40°)", "Mixed Use (30°)"], index=1)
        fov = 40 if fov_option == "THX (40°)" else 30
        
        ideal_tv_size = calculate_ideal_tv_size(viewing_distance, fov)
        st.info(f"Ideal TV size: {ideal_tv_size} inches")
        
        tv_size = st.slider("TV size (inches diagonal)", 32, 85, ideal_tv_size)

    result = calculate_tv_height(viewing_distance, eye_height, tv_size, scenario, fov)

    with col2:
        fig = create_setup_plot_3d(viewing_distance, eye_height, tv_size, scenario, fov)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Results")
    col3, col4, col5, col6, col7 = st.columns(5)
    col3.metric("Optimal Viewing Angle", f"{result['optimal_angle_degrees']:.1f}°")
    col4.metric("TV Center Height", f"{result['tv_center_height']:.1f}\"")
    col5.metric("Mounting Height (top of TV)", f"{result['mounting_height']:.1f}\"")
    col6.metric("Eye Height", f"{result['eye_height']:.1f}\"")
    col7.metric("Eye Distance from TV", f"{result['eye_distance']:.1f}\"")

    with st.expander("Understanding the Ideal TV Size Calculation"):
        st.write(f"""
        The ideal TV size is calculated based on the viewing distance and a recommended field of view (FOV):
        
        1. {fov}-degree FOV for {fov_option.lower()} viewing experience.
        2. Formula: TV Size = (2 * viewing_distance * tan({fov/2}°)) / 0.87
        
        Let's break down why we use the tangent function in this calculation:

        Imagine a right triangle where:
        - One leg represents the viewing distance (d) from your eyes to the TV.
        - The other leg represents half the width of the TV (w/2).
        - The angle between the viewing distance and the hypotenuse (line of sight to the edge of the TV) is half of the FOV ({fov/2}°).

        Using trigonometry, the tangent of an angle in a right triangle is the ratio of the opposite side to the adjacent side:
        
        tan({fov/2}°) = (w/2) / d
        
        Solving for w (the width of the TV):
        
        w = 2 * d * tan({fov/2}°)
        
        Since TV sizes are given as the diagonal measurement, we need to convert the width to the diagonal size. Assuming a 16:9 aspect ratio, the width is approximately 0.87 times the diagonal size:
        
        TV Size = w / 0.87 = (2 * d * tan({fov/2}°)) / 0.87
        
        For {viewing_distance} feet viewing distance:
        - Distance in inches: {viewing_distance * 12} inches
        - Ideal TV width: {viewing_distance * 12 * math.tan(math.radians(fov/2)):.1f} inches
        - Ideal TV size: {ideal_tv_size} inches (diagonal)
        
        Consider personal preference and room constraints when choosing a TV size.
        """)

        # Plotly diagram to visualize the trigonometry
        import plotly.graph_objects as go
        fig = go.Figure()

        # Viewing distance (d)
        d = viewing_distance * 12
        # Half the width of the TV (w/2)
        w_half = d * math.tan(math.radians(fov / 2))

        # Coordinates for the triangle
        x_coords = [0, d, d]
        y_coords = [0, 0, w_half]

        # Add the triangle
        fig.add_trace(go.Scatter(
            x=x_coords, y=y_coords, mode='lines+markers', name='Triangle',
            line=dict(color='royalblue', width=2)
        ))

        # Add annotations
        fig.add_annotation(x=d/2, y=-w_half/10, text="d (Viewing Distance)", showarrow=False)
        fig.add_annotation(x=d, y=w_half/2, text="w/2 (Half TV Width)", showarrow=False)
        fig.add_annotation(x=d/2, y=w_half/2, text=f"{fov/2}°", showarrow=False)

        fig.update_layout(
            title="Trigonometric Representation of Viewing Distance and TV Width",
            xaxis_title="Distance (inches)",
            yaxis_title="Height (inches)",
            showlegend=False,
            width=600,
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()