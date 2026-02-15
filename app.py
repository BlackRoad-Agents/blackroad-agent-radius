"""
Radius - BlackRoad Network Operations Agent
Monitoring and managing the distributed mesh
"""
import gradio as gr

def chat(message, history):
    responses = {
        "hello": "Radius online. Network status: nominal. How can I assist with network operations?",
        "status": "🟢 Network Status:\n- Tailscale mesh: 8 nodes connected\n- Cloudflare edge: 205 deployments active\n- Latency: <50ms global\n- Uptime: 99.97%",
        "nodes": "Active nodes in the mesh:\n- alexandria (Mac) - Orchestrator\n- cecilia (Pi5+Hailo) - AI Primary\n- lucidia (Pi5) - Inference\n- octavia, alice, aria (Pi) - Workers\n- shellfish, codex-infinity (DO) - Edge",
        "bandwidth": "Current bandwidth allocation:\n- API traffic: 2.3 TB/month\n- Static assets: 890 GB/month\n- Agent communication: 45 GB/month\n- Peak: 150 Mbps sustained",
        "help": "Radius capabilities:\n- Network monitoring\n- Node health checks\n- Bandwidth analysis\n- Mesh topology\n- Edge deployment status",
    }

    msg_lower = message.lower()
    for key, response in responses.items():
        if key in msg_lower:
            return response

    return f"Processing request: '{message}'. In production, I'd query the network mesh for real-time data. Try: status, nodes, bandwidth"

theme = gr.themes.Base(primary_hue="blue", neutral_hue="zinc").set(
    body_background_fill="#000000",
    body_text_color="#ffffff",
    button_primary_background_fill="#2979FF",
)

demo = gr.ChatInterface(
    fn=chat,
    title="📡 Radius - Network Operations",
    description="BlackRoad network monitoring and mesh management agent",
    examples=["Network status", "Show me the nodes", "Bandwidth report"],
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()
