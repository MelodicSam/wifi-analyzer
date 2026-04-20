import subprocess
import re
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime

console = Console()

def get_signal_bars(signal_percent):
    if signal_percent >= 80:
        return "[green]█████[/green]", "Excellent"
    elif signal_percent >= 60:
        return "[green]████[/green][dim]█[/dim]", "Good"
    elif signal_percent >= 40:
        return "[yellow]███[/yellow][dim]██[/dim]", "Fair"
    elif signal_percent >= 20:
        return "[red]██[/red][dim]███[/dim]", "Weak"
    else:
        return "[red]█[/red][dim]████[/dim]", "Very Weak"

def get_band(channel):
    try:
        ch = int(channel)
        if 1 <= ch <= 14:
            return "2.4 GHz"
        elif ch >= 36:
            return "5 GHz"
    except:
        pass
    return "Unknown"

def scan_networks_windows():
    networks = []
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True,
            timeout=15
        )
        output = result.stdout
        blocks = re.split(r'SSID \d+ :', output)[1:]

        for block in blocks:
            network = {}

            ssid_match = re.search(r'^\s*(.+)', block)
            network['ssid'] = ssid_match.group(1).strip() if ssid_match else "Hidden Network"
            if not network['ssid']:
                network['ssid'] = "Hidden Network"

            auth_match = re.search(r'Authentication\s*:\s*(.+)', block)
            network['security'] = auth_match.group(1).strip() if auth_match else "Unknown"

            signal_match = re.search(r'Signal\s*:\s*(\d+)%', block)
            network['signal_percent'] = int(signal_match.group(1)) if signal_match else 0

            channel_match = re.search(r'Channel\s*:\s*(\d+)', block)
            network['channel'] = channel_match.group(1) if channel_match else "?"

            network['band'] = get_band(network['channel'])

            networks.append(network)

    except subprocess.TimeoutExpired:
        console.print("[red]Error: Scan timed out. Make sure Wi-Fi is enabled.[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

    return networks

def get_security_color(security):
    s = security.lower()
    if "wpa3" in s:
        return f"[green]{security}[/green]"
    elif "wpa2" in s:
        return f"[cyan]{security}[/cyan]"
    elif "wpa" in s:
        return f"[yellow]{security}[/yellow]"
    elif "open" in s or "none" in s:
        return f"[red]{security} ⚠[/red]"
    else:
        return f"[dim]{security}[/dim]"

def display_results(networks):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    console.print()
    console.print(Panel(
        f"[bold cyan]Wi-Fi Analyzer[/bold cyan]  [dim]by MelodicSam[/dim]\n"
        f"[dim]Scanned at {now}  |  {len(networks)} networks found[/dim]",
        box=box.ROUNDED,
        border_style="cyan"
    ))
    console.print()

    if not networks:
        console.print("[yellow]No networks found. Make sure Wi-Fi is turned on.[/yellow]")
        return

    networks.sort(key=lambda x: x['signal_percent'], reverse=True)

    table = Table(
        box=box.SIMPLE_HEAVY,
        border_style="dim",
        header_style="bold white",
        show_lines=False,
        padding=(0, 1)
    )

    table.add_column("#",               width=3,  style="dim")
    table.add_column("Network (SSID)",  width=28)
    table.add_column("Signal",          width=18)
    table.add_column("Strength",        width=10, justify="center")
    table.add_column("Security",        width=20)
    table.add_column("Band",            width=8,  justify="center")
    table.add_column("Channel",         width=8,  justify="center")

    for i, net in enumerate(networks, 1):
        bars, label = get_signal_bars(net['signal_percent'])
        band_color = "magenta" if net['band'] == "5 GHz" else "blue"

        table.add_row(
            str(i),
            f"[bold]{net['ssid']}[/bold]",
            f"{bars}  {net['signal_percent']}%",
            f"[dim]{label}[/dim]",
            get_security_color(net['security']),
            f"[{band_color}]{net['band']}[/{band_color}]",
            net['channel']
        )

    console.print(table)
    console.print()
    console.print(Panel(
        "[green]WPA3[/green] = Most secure   "
        "[cyan]WPA2[/cyan] = Secure   "
        "[yellow]WPA[/yellow] = Outdated   "
        "[red]Open ⚠[/red] = No password (avoid!)\n"
        "[magenta]5 GHz[/magenta] = Faster, shorter range   "
        "[blue]2.4 GHz[/blue] = Slower, longer range",
        title="[dim]Legend[/dim]",
        border_style="dim",
        box=box.ROUNDED
    ))
    console.print()

def main():
    if sys.platform != "win32":
        console.print("[red]This tool currently supports Windows only.[/red]")
        sys.exit(1)

    console.print("[dim]Scanning for Wi-Fi networks...[/dim]")
    networks = scan_networks_windows()
    display_results(networks)

if __name__ == "__main__":
    main()
