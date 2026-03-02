import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(1, 1, figsize=(22, 16))
ax.set_xlim(0, 22)
ax.set_ylim(0, 16)
ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# ── helpers ──────────────────────────────────────────────────────────────────
def box(x, y, w, h, fc, ec, radius=0.3, alpha=1.0):
    rect = FancyBboxPatch((x, y), w, h,
                          boxstyle=f"round,pad=0.05,rounding_size={radius}",
                          facecolor=fc, edgecolor=ec,
                          linewidth=2, alpha=alpha, zorder=3)
    ax.add_patch(rect)

def txt(x, y, s, size=9, color='white', bold=False, ha='center', va='center', zorder=5):
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=zorder, fontfamily='monospace')

def arrow(x1, y1, x2, y2, color='#58a6ff', lw=1.8, style='->', bidirectional=False):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, connectionstyle='arc3,rad=0.0'),
                zorder=4)
    if bidirectional:
        ax.annotate('', xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle=style, color=color,
                                    lw=lw, connectionstyle='arc3,rad=0.0'),
                    zorder=4)

# ── TITLE ────────────────────────────────────────────────────────────────────
txt(11, 15.3, '⚓  KUBERNETES ARCHITECTURE  —  THE CARGO SHIP',
    size=16, bold=True, color='#58a6ff')
txt(11, 14.85, 'Control Plane (Captain\'s Bridge)  +  Worker Nodes (Cargo Decks)',
    size=10, color='#8b949e')

# ── USER / kubectl ────────────────────────────────────────────────────────────
box(0.4, 12.8, 2.5, 1.4, '#21262d', '#58a6ff', radius=0.4)
txt(1.65, 13.7, '👤 Developer', size=9, bold=True, color='#58a6ff')
txt(1.65, 13.3, 'kubectl', size=8, color='#8b949e')
txt(1.65, 12.95, 'apply / get / delete', size=7, color='#8b949e')

# ── CONTROL PLANE outer box ───────────────────────────────────────────────────
box(3.4, 8.5, 10.8, 6.0, '#161b22', '#f0883e', radius=0.5, alpha=0.95)
txt(8.8, 14.1, '🚢  CONTROL PLANE  (Captain\'s Bridge — Master Node)',
    size=11, bold=True, color='#f0883e')

# API Server
box(4.0, 11.4, 3.2, 2.4, '#1f2937', '#58a6ff', radius=0.35)
txt(5.6, 13.3,  '📡 API SERVER',  size=10, bold=True, color='#58a6ff')
txt(5.6, 12.85, '"The Captain"',  size=8,  color='#ffd700')
txt(5.6, 12.45, 'Front door for ALL', size=7.5, color='#c9d1d9')
txt(5.6, 12.1,  'commands & requests', size=7.5, color='#c9d1d9')
txt(5.6, 11.75, 'Validates & routes', size=7.5, color='#c9d1d9')
txt(5.6, 11.45, 'every operation',   size=7.5, color='#c9d1d9')

# etcd
box(7.6, 11.4, 3.0, 2.4, '#1f2937', '#3fb950', radius=0.35)
txt(9.1, 13.3,  '📖 etcd',         size=10, bold=True, color='#3fb950')
txt(9.1, 12.85, '"The Logbook"',   size=8,  color='#ffd700')
txt(9.1, 12.45, 'Stores ALL cluster', size=7.5, color='#c9d1d9')
txt(9.1, 12.1,  'state & config', size=7.5, color='#c9d1d9')
txt(9.1, 11.75, 'Key-value store', size=7.5, color='#c9d1d9')
txt(9.1, 11.45, 'Source of truth', size=7.5, color='#c9d1d9')

# Scheduler
box(4.0, 8.9, 3.0, 2.2, '#1f2937', '#d2a8ff', radius=0.35)
txt(5.5, 10.6,  '🗓 SCHEDULER',   size=10, bold=True, color='#d2a8ff')
txt(5.5, 10.15, '"Cargo Loader"', size=8,  color='#ffd700')
txt(5.5, 9.75,  'Picks BEST node', size=7.5, color='#c9d1d9')
txt(5.5, 9.4,   'for each new pod', size=7.5, color='#c9d1d9')
txt(5.5, 9.05,  'Checks CPU/RAM', size=7.5, color='#c9d1d9')

# Controller Manager
box(7.4, 8.9, 3.4, 2.2, '#1f2937', '#ff7b72', radius=0.35)
txt(9.1, 10.6,  '🔍 CTRL MANAGER', size=9.5, bold=True, color='#ff7b72')
txt(9.1, 10.15, '"Ship Inspector"',  size=8,   color='#ffd700')
txt(9.1, 9.75,  'Watchdog 24/7',    size=7.5,  color='#c9d1d9')
txt(9.1, 9.4,   'Desired vs Actual', size=7.5, color='#c9d1d9')
txt(9.1, 9.05,  'Auto-heals pods',  size=7.5,  color='#c9d1d9')

# Cloud Controller Manager (small, on right of control plane)
box(11.0, 9.6, 2.8, 1.6, '#1f2937', '#79c0ff', radius=0.35)
txt(12.4, 10.8, '☁ CLOUD CTL', size=9, bold=True, color='#79c0ff')
txt(12.4, 10.4, 'Talks to AWS/', size=7.5, color='#c9d1d9')
txt(12.4, 10.05,'GCP / Azure', size=7.5, color='#c9d1d9')
txt(12.4, 9.7,  '"Port Agent"', size=7.5, color='#ffd700')

# Internal arrows inside control plane
arrow(7.2, 12.6, 7.6, 12.6, color='#58a6ff', bidirectional=True)   # API ↔ etcd
arrow(5.6, 11.4, 5.5, 11.1, color='#d2a8ff')                       # API → Scheduler
arrow(8.0, 11.4, 9.0, 11.1, color='#ff7b72')                       # API → CtrlMgr
arrow(10.6, 10.5, 11.0, 10.5, color='#79c0ff')                     # API → Cloud

# ── WORKER NODES ──────────────────────────────────────────────────────────────
worker_configs = [
    (0.3,  4.8, '#161b22', '#3fb950', 'WORKER NODE 1', '🖥',
     [('webapp', '#1f6feb'), ('api',    '#388bfd'), ('db',  '#1f6feb')]),
    (7.6,  4.8, '#161b22', '#3fb950', 'WORKER NODE 2', '🖥',
     [('nginx',  '#1f6feb'), ('cache', '#388bfd')]),
    (14.4, 4.8, '#161b22', '#3fb950', 'WORKER NODE 3', '🖥',
     [('worker', '#1f6feb'), ('cron',  '#388bfd'), ('ml', '#1f6feb')]),
]

for wx, wy, wfc, wec, wlabel, icon, pods in worker_configs:
    ww = 6.8
    box(wx, wy, ww, 5.6, wfc, wec, radius=0.5)
    txt(wx + ww/2, wy + 5.35, f'{icon}  {wlabel}', size=10, bold=True, color='#3fb950')

    # Kubelet
    box(wx+0.2, wy+4.0, 2.9, 1.0, '#21262d', '#d2a8ff', radius=0.25)
    txt(wx+1.65, wy+4.65, '🤖 Kubelet', size=8.5, bold=True, color='#d2a8ff')
    txt(wx+1.65, wy+4.2,  '"Deck Supervisor"', size=7, color='#ffd700')

    # Kube-proxy
    box(wx+3.3, wy+4.0, 3.1, 1.0, '#21262d', '#ff7b72', radius=0.25)
    txt(wx+4.85, wy+4.65, '🔀 Kube-proxy', size=8.5, bold=True, color='#ff7b72')
    txt(wx+4.85, wy+4.2,  '"Traffic Cop"', size=7, color='#ffd700')

    # Container Runtime
    box(wx+0.2, wy+2.8, 6.1, 0.9, '#21262d', '#f0883e', radius=0.25)
    txt(wx+3.25, wy+3.35, '⚙  Container Runtime  (containerd / Docker)', size=8, bold=True, color='#f0883e')
    txt(wx+3.25, wy+2.95, '"Crane Operator — Actually runs the containers"', size=7, color='#ffd700')

    # Pods row
    pod_colors = [p[1] for p in pods]
    pod_names  = [p[0] for p in pods]
    total_pods = len(pods)
    pod_w = 1.7
    gap   = (ww - 0.4 - total_pods * pod_w) / (total_pods + 1)
    for i, (pname, pc) in enumerate(pods):
        px = wx + 0.2 + gap + i * (pod_w + gap)
        box(px, wy+0.2, pod_w, 2.3, '#0d1117', pc, radius=0.3)
        txt(px + pod_w/2, wy+2.0,  '📦 POD',  size=8,   bold=True, color='#58a6ff')
        txt(px + pod_w/2, wy+1.6,  pname,      size=8.5, bold=True, color='white')
        box(px+0.15, wy+0.45, pod_w-0.3, 0.85, '#161b22', '#388bfd', radius=0.2)
        txt(px + pod_w/2, wy+0.9,  '🐋 Container', size=6.5, color='#79c0ff')
        txt(px + pod_w/2, wy+0.6,  'running', size=6, color='#3fb950')

# ── SERVICES / INGRESS strip ──────────────────────────────────────────────────
box(0.3, 3.0, 21.0, 1.5, '#161b22', '#ffd700', radius=0.4)
txt(4.0, 3.95, '🌐 SERVICE (ClusterIP)', size=9, bold=True, color='#ffd700')
txt(4.0, 3.5,  'Stable address → pods', size=7.5, color='#c9d1d9')
txt(10.8, 3.95, '⚖  LoadBalancer / NodePort', size=9, bold=True, color='#ffd700')
txt(10.8, 3.5,  'External traffic entry point', size=7.5, color='#c9d1d9')
txt(17.5, 3.95, '🚪 INGRESS', size=9, bold=True, color='#ffd700')
txt(17.5, 3.5,  '/api → api-svc  /web → web-svc', size=7.5, color='#c9d1d9')

# ── STORAGE / CONFIG strip ────────────────────────────────────────────────────
box(0.3, 1.3, 21.0, 1.4, '#161b22', '#8b949e', radius=0.4)
txt(3.5,  2.3, '💾 Persistent Volume', size=9, bold=True, color='#8b949e')
txt(3.5,  1.85,'Storage surviving pod death', size=7.5, color='#c9d1d9')
txt(9.5,  2.3, '⚙  ConfigMap', size=9, bold=True, color='#8b949e')
txt(9.5,  1.85,'App config & env vars', size=7.5, color='#c9d1d9')
txt(14.5, 2.3, '🔐 Secret', size=9, bold=True, color='#8b949e')
txt(14.5, 1.85,'Passwords & API keys (encrypted)', size=7.5, color='#c9d1d9')
txt(19.5, 2.3, '📁 Namespace', size=9, bold=True, color='#8b949e')
txt(19.5, 1.85,'Virtual cluster sections', size=7.5, color='#c9d1d9')

# ── INTERNET box ──────────────────────────────────────────────────────────────
box(15.5, 12.4, 5.8, 1.8, '#161b22', '#58a6ff', radius=0.4)
txt(18.4, 13.65, '🌍 INTERNET / Users', size=10, bold=True, color='#58a6ff')
txt(18.4, 13.2,  'HTTP requests to your app', size=8, color='#c9d1d9')

# ── LEGEND ────────────────────────────────────────────────────────────────────
legend_items = [
    ('#f0883e', 'Control Plane'),
    ('#3fb950', 'Worker Node'),
    ('#58a6ff', 'API / Network'),
    ('#d2a8ff', 'Kubelet'),
    ('#ff7b72', 'Controllers'),
    ('#ffd700', 'Services'),
]
lx, ly = 15.5, 11.5
txt(lx + 2.8, ly + 0.2, 'LEGEND', size=8, bold=True, color='#8b949e')
for i, (color, label) in enumerate(legend_items):
    col = i % 3
    row = i // 3
    bx = lx + col * 1.95
    by = ly - row * 0.55
    box(bx, by - 0.35, 0.35, 0.35, color, color, radius=0.1)
    txt(bx + 0.55, by - 0.18, label, size=7.5, color='#c9d1d9', ha='left')

# ── ARROWS: kubectl → API Server ──────────────────────────────────────────────
arrow(2.9, 13.5, 4.0, 12.8, color='#58a6ff', lw=2.0)
txt(3.3, 13.25, 'kubectl', size=7, color='#58a6ff')

# API Server → Scheduler (already inside box)
# API Server → Worker Kubelets
for wx_center in [3.7, 11.0, 17.8]:
    arrow(7.1, 10.5, wx_center, 10.4, color='#3fb950', lw=1.5)

# Internet → Ingress/Service
arrow(16.5, 12.4, 14.5, 4.55, color='#58a6ff', lw=1.8, style='->')

# ── FOOTER ────────────────────────────────────────────────────────────────────
txt(11, 0.65, '⚓  The Ship Analogy:  Control Plane = Captain\'s Bridge  |  Worker Nodes = Cargo Decks  |  Pods = Shipping Containers',
    size=8, color='#8b949e')

plt.tight_layout(pad=0.2)
plt.savefig('K8S_Architecture.jpeg', dpi=150, bbox_inches='tight',
            facecolor='#0d1117', edgecolor='none', format='jpeg',
            pil_kwargs={'quality': 95})
plt.close()
print("K8S_Architecture.jpeg created successfully!")
