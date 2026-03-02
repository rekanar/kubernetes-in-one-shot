import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(24, 20))
ax.set_xlim(-12, 12)
ax.set_ylim(-11, 11)
ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# ─── helpers ──────────────────────────────────────────────────────────────────
def node(x, y, label, sublabel='', fc='#1f6feb', ec='#58a6ff',
         r=1.0, fontsize=10, subfontsize=7.5):
    circle = plt.Circle((x, y), r, color=fc, ec=ec, linewidth=2.5, zorder=3)
    ax.add_patch(circle)
    if sublabel:
        ax.text(x, y + 0.18, label, ha='center', va='center',
                fontsize=fontsize, color='white', fontweight='bold',
                fontfamily='monospace', zorder=4)
        ax.text(x, y - 0.28, sublabel, ha='center', va='center',
                fontsize=subfontsize, color='#ffd700',
                fontfamily='monospace', zorder=4)
    else:
        ax.text(x, y, label, ha='center', va='center',
                fontsize=fontsize, color='white', fontweight='bold',
                fontfamily='monospace', zorder=4)

def rect_node(x, y, w, h, label, sublabel='', fc='#21262d', ec='#58a6ff',
              fontsize=8.5, subfontsize=7):
    rect = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                    boxstyle="round,pad=0.08,rounding_size=0.2",
                                    facecolor=fc, edgecolor=ec,
                                    linewidth=1.8, zorder=3)
    ax.add_patch(rect)
    if sublabel:
        ax.text(x, y + 0.18, label, ha='center', va='center',
                fontsize=fontsize, color='white', fontweight='bold',
                fontfamily='monospace', zorder=4)
        ax.text(x, y - 0.22, sublabel, ha='center', va='center',
                fontsize=subfontsize, color='#ffd700',
                fontfamily='monospace', zorder=4)
    else:
        ax.text(x, y, label, ha='center', va='center',
                fontsize=fontsize, color='white', fontweight='bold',
                fontfamily='monospace', zorder=4)

def line(x1, y1, x2, y2, color='#30363d', lw=2.0, style='-'):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw,
            linestyle=style, zorder=1, alpha=0.85)

def curved_line(x1, y1, x2, y2, color='#30363d', lw=1.8):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 + 0.3
    t = np.linspace(0, 1, 50)
    bx = (1-t)**2 * x1 + 2*(1-t)*t * mx + t**2 * x2
    by = (1-t)**2 * y1 + 2*(1-t)*t * my + t**2 * y2
    ax.plot(bx, by, color=color, lw=lw, zorder=1, alpha=0.85)

# ─── TITLE ────────────────────────────────────────────────────────────────────
ax.text(0, 10.4, '⚓  KUBERNETES — MIND MAP',
        ha='center', va='center', fontsize=20, color='#58a6ff',
        fontweight='bold', fontfamily='monospace', zorder=5)
ax.text(0, 9.8, 'The Cargo Ship  |  Captain\'s Bridge  +  Cargo Decks  +  Shipping Containers',
        ha='center', va='center', fontsize=10, color='#8b949e',
        fontfamily='monospace', zorder=5)

# ─── CENTRE NODE ─────────────────────────────────────────────────────────────
node(0, 0, 'KUBERNETES', '☸ Cluster', fc='#1c2d4c', ec='#58a6ff', r=1.55, fontsize=13)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 1 — CONTROL PLANE  (top-left)
# ═══════════════════════════════════════════════════════════════════════════════
cpx, cpy = -5.5, 5.8
line(0, 1.55, cpx, cpy - 1.1, color='#f0883e', lw=3)
node(cpx, cpy, 'CONTROL', 'PLANE', fc='#2d1b00', ec='#f0883e', r=1.3, fontsize=11)

cp_children = [
    (-9.5, 8.0,  '📡 API',    'SERVER',    '"The Captain"',   '#1a2433', '#58a6ff'),
    (-7.5, 8.5,  '📖 etcd',   '',          '"The Logbook"',   '#1a331a', '#3fb950'),
    (-5.0, 8.5,  '🗓 SCHED-', 'ULER',      '"Cargo Loader"',  '#2a1a33', '#d2a8ff'),
    (-3.0, 8.0,  '🔍 CTRL',   'MANAGER',   '"Ship Inspector"','#331a1a', '#ff7b72'),
]
for cx, cy, l1, l2, sub, fc, ec in cp_children:
    line(cpx, cpy + 1.3, cx, cy - 0.85, color=ec, lw=1.8)
    label = l1 + (' ' + l2 if l2 else '')
    node(cx, cy, label.strip(), sub, fc=fc, ec=ec, r=0.95, fontsize=8, subfontsize=6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 2 — WORKER NODES  (top-right)
# ═══════════════════════════════════════════════════════════════════════════════
wnx, wny = 5.5, 5.8
line(0, 1.55, wnx, wny - 1.1, color='#3fb950', lw=3)
node(wnx, wny, 'WORKER', 'NODES', fc='#1a2d1a', ec='#3fb950', r=1.3, fontsize=11)

wn_children = [
    (3.0, 8.0,  '🤖 KUBELET', '"Deck Supervisor"',  '#1a1a2d', '#d2a8ff'),
    (5.5, 8.5,  '🔀 KUBE-',   '"Traffic Cop"',       '#2d1a1a', '#ff7b72'),
    (8.0, 8.5,  '⚙ CONTAINER', '"Crane Operator"',   '#1a1f1a', '#f0883e'),
    (10.5,8.0,  '📦 PODS',    '"Shipping Containers"','#1a1a2d', '#58a6ff'),
]
labels_fix = [
    (3.0, 8.0,  '🤖 Kubelet',  '"Deck Supervisor"',  '#1a1a2d', '#d2a8ff'),
    (5.5, 8.5,  '🔀 Kube-Proxy','"Traffic Cop"',      '#2d1a1a', '#ff7b72'),
    (8.0, 8.5,  '⚙ Runtime',   '"Crane Operator"',   '#1a1f1a', '#f0883e'),
    (10.5,8.0,  '📦 Pods',     '"Containers"',        '#1a1a2d', '#58a6ff'),
]
for cx, cy, label, sub, fc, ec in labels_fix:
    line(wnx, wny + 1.3, cx, cy - 0.9, color=ec, lw=1.8)
    node(cx, cy, label, sub, fc=fc, ec=ec, r=0.95, fontsize=8, subfontsize=6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 3 — WORKLOADS  (left)
# ═══════════════════════════════════════════════════════════════════════════════
wlx, wly = -7.5, 0.0
line(-1.55, 0, wlx + 1.2, wly, color='#d2a8ff', lw=3)
node(wlx, wly, 'WORKLOAD', 'OBJECTS', fc='#1e1a2d', ec='#d2a8ff', r=1.35, fontsize=10)

wl_items = [
    (-10.8,  2.2, '🔁 ReplicaSet', '"Always N copies"',  '#1a1a2d', '#d2a8ff'),
    (-10.8,  0.0, '🚀 Deployment', '"Rolling updates"',  '#1a1a2d', '#79c0ff'),
    (-10.8, -2.2, '⚡ StatefulSet', '"Ordered pods"',    '#1a1a2d', '#ff7b72'),
    (-7.5,  -3.5, '🔄 DaemonSet',  '"1 pod per node"',   '#1a1a2d', '#3fb950'),
    (-4.8,  -2.8, '✅ Job / CronJob','"Run once / timed"','#1a1a2d','#f0883e'),
]
for cx, cy, label, sub, fc, ec in wl_items:
    curved_line(wlx, wly, cx, cy, color=ec, lw=1.6)
    node(cx, cy, label, sub, fc=fc, ec=ec, r=1.0, fontsize=7.5, subfontsize=6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 4 — NETWORKING  (right)
# ═══════════════════════════════════════════════════════════════════════════════
nwx, nwy = 7.5, 0.0
line(1.55, 0, nwx - 1.2, nwy, color='#ffd700', lw=3)
node(nwx, nwy, 'NETWORKING', '', fc='#2d2a00', ec='#ffd700', r=1.35, fontsize=10)

nw_items = [
    (10.5,  2.5, '🌐 Service',   '"Stable address"',  '#2d2a00', '#ffd700'),
    (10.5,  0.5, '🚪 Ingress',   '"Harbour gate"',    '#2d2a00', '#f0883e'),
    (10.5, -1.5, '🔗 ClusterIP', '"Internal route"',  '#1a2433', '#58a6ff'),
    (8.5,  -3.5, '⚖ LoadBalancer','"Cloud traffic"',  '#1a1a2d', '#79c0ff'),
]
for cx, cy, label, sub, fc, ec in nw_items:
    curved_line(nwx, nwy, cx, cy, color=ec, lw=1.6)
    node(cx, cy, label, sub, fc=fc, ec=ec, r=1.0, fontsize=7.5, subfontsize=6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 5 — CONFIG & STORAGE  (bottom-left)
# ═══════════════════════════════════════════════════════════════════════════════
csx, csy = -5.5, -5.8
line(0, -1.55, csx, csy + 1.1, color='#3fb950', lw=3)
node(csx, csy, 'CONFIG &', 'STORAGE', fc='#1a2d1a', ec='#3fb950', r=1.3, fontsize=10)

cs_items = [
    (-9.0, -7.8, '⚙ ConfigMap',  '"Public settings"',  '#1a2d1a', '#3fb950'),
    (-6.5, -8.5, '🔐 Secret',    '"Passwords/keys"',   '#2d1a1a', '#ff7b72'),
    (-4.0, -8.5, '💾 PV / PVC',  '"Persistent storage"','#1a1f2d','#79c0ff'),
    (-2.0, -7.8, '📁 Namespace', '"Virtual sections"', '#2a1a33', '#d2a8ff'),
]
for cx, cy, label, sub, fc, ec in cs_items:
    line(csx, csy - 1.3, cx, cy + 0.9, color=ec, lw=1.8)
    node(cx, cy, label, sub, fc=fc, ec=ec, r=0.95, fontsize=8, subfontsize=6.5)

# ═══════════════════════════════════════════════════════════════════════════════
# BRANCH 6 — KEY FEATURES  (bottom-right)
# ═══════════════════════════════════════════════════════════════════════════════
kfx, kfy = 5.5, -5.8
line(0, -1.55, kfx, kfy + 1.1, color='#58a6ff', lw=3)
node(kfx, kfy, 'KEY', 'FEATURES', fc='#1a1f2d', ec='#58a6ff', r=1.3, fontsize=11)

kf_items = [
    (3.0, -7.8,  '🔄 Auto-Heal',  '"Restarts crashed pods"', '#1a2433', '#58a6ff'),
    (5.5, -8.5,  '📈 Auto-Scale', '"HPA — traffic-based"',   '#1a2433', '#3fb950'),
    (8.0, -8.5,  '🔄 Rolling',    '"Zero-downtime deploy"',  '#1a2433', '#f0883e'),
    (10.5,-7.8,  '⚖ Load Bal.',   '"Spread traffic evenly"', '#1a2433', '#ffd700'),
]
for cx, cy, label, sub, fc, ec in kf_items:
    line(kfx, kfy - 1.3, cx, cy + 0.9, color=ec, lw=1.8)
    node(cx, cy, label, sub, fc=fc, ec=ec, r=0.95, fontsize=8, subfontsize=6.5)

# ─── DOCKER vs K8S callout ────────────────────────────────────────────────────
rect_node(-3.0, -0.5, 2.4, 1.2, '🐋 Docker', 'Packs the app', fc='#1a2433', ec='#1d76db', fontsize=8)
line(-1.55, 0.0, -1.8, -0.5, color='#1d76db', lw=1.5, style='--')
ax.text(-1.5, -1.1, 'Docker = Lunchbox\nKubernetes = Cafeteria Mgr',
        ha='center', va='center', fontsize=7.5, color='#ffd700',
        fontfamily='monospace', zorder=4,
        bbox=dict(boxstyle='round,pad=0.3', fc='#161b22', ec='#ffd700', lw=1.2))

# ─── FOOTER ───────────────────────────────────────────────────────────────────
ax.text(0, -10.5,
        'Control Plane = Captain\'s Bridge  •  Worker Node = Cargo Deck  •  Pod = Shipping Container  •  Service = Loading Dock',
        ha='center', va='center', fontsize=9, color='#8b949e', fontfamily='monospace', zorder=5)

plt.tight_layout(pad=0.2)
plt.savefig('K8S_MindMap.jpeg', dpi=150, bbox_inches='tight',
            facecolor='#0d1117', edgecolor='none', format='jpeg',
            pil_kwargs={'quality': 95})
plt.close()
print("K8S_MindMap.jpeg created successfully!")
