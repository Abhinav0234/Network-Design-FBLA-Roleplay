import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change label from "EXAMPLE ROLEPLAY SCENARIO" to "PLUG & PLAY SCRIPT"
html = html.replace('EXAMPLE ROLEPLAY SCENARIO', 'PLUG &amp; PLAY SCRIPT')

# Replace each specific scenario with a generalizable template
replacements = [
    # Star Topology
    (
        '<strong>🏢 Small Law Firm — 25 employees:</strong> "I\'d recommend a star topology with a managed switch at the center. Each workstation connects directly, so if one attorney\'s machine goes down, it won\'t affect the rest of the office. We can easily add new hires by plugging into open switch ports."',
        '🎤 <em>"I\'d recommend a <strong>star topology</strong> with a managed switch at the center. Each workstation connects directly to the switch, so if any single device fails, the rest of the network stays up. As <strong>[company]</strong> grows and adds new <strong>[employees/devices]</strong>, we simply plug into open switch ports — no network redesign needed."</em>'
    ),
    # Mesh Topology
    (
        '<strong>🏥 Regional Hospital Network:</strong> "Patient data systems require near-100% uptime. I\'d use a partial mesh topology for the core network, ensuring multiple redundant paths so that if any single link fails, traffic automatically reroutes without impacting clinical operations."',
        '🎤 <em>"Given that <strong>[company]</strong> requires near-100% uptime for <strong>[critical system]</strong>, I\'d implement a <strong>partial mesh topology</strong> for the core network. This provides multiple redundant paths, so if any single link fails, traffic automatically reroutes — ensuring zero disruption to <strong>[key operations]</strong>."</em>'
    ),
    # VLAN Segmentation
    (
        '<strong>🏦 Accounting Firm — 3 departments:</strong> "I\'d configure three VLANs: VLAN 10 for Finance, VLAN 20 for HR, and VLAN 30 for Guest Wi-Fi. This ensures that sensitive payroll data in HR can\'t be accessed from the guest network, meeting compliance requirements without installing separate physical switches."',
        '🎤 <em>"I\'d configure separate VLANs for each department — for example, VLAN 10 for <strong>[Dept A]</strong>, VLAN 20 for <strong>[Dept B]</strong>, and VLAN 30 for Guest Wi-Fi. This ensures that sensitive <strong>[data type]</strong> can\'t be accessed from other segments, meeting <strong>[compliance requirement]</strong> without separate physical infrastructure."</em>'
    ),
    # Firewall
    (
        '<strong>🏪 Retail Chain with Online Store:</strong> "I\'d deploy a Next-Gen Firewall at the network perimeter using a restrictive policy — blocking all traffic except ports 80, 443, and 25 for web and email. The NGFW\'s deep packet inspection will detect and block malware, SQL injection, and credit card skimming attempts on the e-commerce platform."',
        '🎤 <em>"I\'d deploy a <strong>Next-Gen Firewall</strong> at the network perimeter using a <strong>restrictive policy</strong> — denying all traffic by default and only allowing what\'s explicitly needed, like ports 80 and 443 for web. The NGFW\'s deep packet inspection will protect <strong>[company]</strong>\'s <strong>[assets/data]</strong> from threats like malware, phishing, and unauthorized access."</em>'
    ),
    # VPN
    (
        '<strong>💼 Marketing Agency — 15 remote staff:</strong> "Remote employees will connect via SSL/TLS VPN through their browser, creating an encrypted tunnel to our office network. This ensures that client files and campaign data remain secure even when accessed from public Wi-Fi at coffee shops."',
        '🎤 <em>"<strong>[Remote/traveling employees]</strong> will connect via <strong>SSL/TLS VPN</strong>, creating an encrypted tunnel to the office network. This ensures that <strong>[sensitive data type]</strong> remains fully secure even when accessed from untrusted networks like public Wi-Fi or home internet connections."</em>'
    ),
    # DHCP
    (
        '<strong>🎓 School Campus — 500 devices:</strong> "With hundreds of student laptops connecting daily, manual IP assignment is impractical. A DHCP server will dynamically assign addresses from a pool. Servers and printers will use DHCP reservations so their IPs never change, but are still centrally managed."',
        '🎤 <em>"With <strong>[number]</strong> devices on the network, manual IP configuration would be impractical and error-prone. A <strong>DHCP server</strong> will dynamically assign addresses using the DORA process. Critical devices like servers and printers will use <strong>DHCP reservations</strong> so their IPs remain consistent but are still centrally managed."</em>'
    ),
    # DNS
    (
        '<strong>🏢 Corporate Office:</strong> "We\'ll configure an internal DNS server integrated with Active Directory so employees can access the file server as \\\\fileserver.company.local instead of memorizing 192.168.1.10. External DNS will point our company domain to the web server in the DMZ."',
        '🎤 <em>"We\'ll configure an <strong>internal DNS server</strong> integrated with Active Directory so employees can access resources by name instead of memorizing IP addresses. If <strong>[company]</strong> hosts any public services, external DNS records will point the domain to the appropriate servers."</em>'
    ),
    # Active Directory
    (
        '<strong>📋 Insurance Company — 75 employees:</strong> "Active Directory will manage all user accounts centrally. Group Policy will enforce password complexity, screen lock timeouts, and prevent unauthorized software installation — ensuring HIPAA compliance for handling patient insurance data."',
        '🎤 <em>"<strong>Active Directory</strong> will manage all user accounts centrally. <strong>Group Policy</strong> will enforce password complexity, screen lock timeouts, and software restrictions across every workstation. This ensures <strong>[compliance standard]</strong> compliance and gives IT full control over who accesses what on the network."</em>'
    ),
    # DMZ
    (
        '<strong>🛒 E-Commerce Company:</strong> "The web server handling customer orders will be placed in a DMZ between two firewalls. If an attacker compromises the web server, the second firewall prevents them from reaching the internal database server containing customer payment information."',
        '🎤 <em>"Any public-facing servers — like <strong>[web/email/FTP]</strong> — will be placed in a <strong>DMZ</strong> between two firewalls. If an attacker compromises a DMZ server, the second firewall prevents lateral movement into the internal LAN where <strong>[sensitive data/systems]</strong> reside."</em>'
    ),
    # QoS
    (
        '<strong>📱 Call Center — 50 agents:</strong> "QoS rules on our managed switches will prioritize VoIP traffic over general web browsing. This ensures that when an agent is on a customer call, their voice quality won\'t degrade even if another employee is downloading a large file."',
        '🎤 <em>"<strong>QoS rules</strong> on our managed switches will prioritize <strong>[VoIP/video/real-time traffic]</strong> over general web browsing and file downloads. This guarantees that <strong>[critical application]</strong> always has the bandwidth it needs, even during peak usage periods."</em>'
    ),
    # RAID 5 + NAS/SAN
    (
        '<strong>📁 Architecture Firm — large CAD files:</strong> "The file server will use RAID 5 with 4 drives — if any single drive fails, data stays accessible while we hot-swap the replacement. A NAS device in each office provides local file access, with nightly replication to the main SAN at headquarters."',
        '🎤 <em>"The file server will use <strong>RAID 5</strong> with 4 drives — if any single drive fails, data stays fully accessible while we hot-swap the replacement with zero downtime. A <strong>[NAS for file sharing / SAN for databases]</strong> provides centralized, fault-tolerant storage for <strong>[company]</strong>\'s <strong>[data type]</strong>."</em>'
    ),
    # UPS + Backup
    (
        '<strong>⚡ Dental Practice — patient records:</strong> "A UPS on each server rack ensures graceful shutdown during power outages. Full backups run every Sunday night; incremental backups run every weeknight. Backups replicate to AWS S3 cloud storage following the 3-2-1 rule, with an RPO of 24 hours and RTO of 4 hours."',
        '🎤 <em>"A <strong>UPS</strong> on each server rack ensures graceful shutdown during power outages. <strong>Full backups</strong> run weekly; <strong>incremental backups</strong> run nightly. All backups replicate to cloud storage following the <strong>3-2-1 rule</strong>. Our target is an <strong>RPO of 24 hours</strong> (max data loss) and <strong>RTO of 4 hours</strong> (max downtime)."</em>'
    ),
    # Zero Trust
    (
        '<strong>🏛️ Government Contractor:</strong> "We\'ll implement Zero Trust principles — every access request is verified regardless of whether the user is on-site or remote. MFA is required for all logins, network micro-segmentation limits lateral movement, and continuous monitoring logs all access attempts for audit review."',
        '🎤 <em>"We\'ll implement <strong>Zero Trust</strong> principles — every access request is verified regardless of whether the user is on-site or remote. <strong>MFA</strong> is required for all logins, <strong>micro-segmentation</strong> limits lateral movement if a breach occurs, and continuous monitoring logs all access for <strong>[audit/compliance]</strong> review."</em>'
    ),
    # Load Balancer
    (
        '<strong>🛒 Online Retailer — Black Friday prep:</strong> "A load balancer in front of three web servers uses round-robin distribution. During peak shopping, if traffic doubles, we add a fourth server and the load balancer automatically includes it. If any server crashes, it\'s removed from the pool within seconds."',
        '🎤 <em>"A <strong>load balancer</strong> in front of multiple <strong>[web/application]</strong> servers distributes traffic using round-robin. If <strong>[company]</strong> experiences traffic spikes, we simply add another server and the load balancer includes it automatically. If any server fails, it\'s removed from the pool within seconds — zero downtime."</em>'
    ),
    # WPA3 + Wireless
    (
        '<strong>🎓 School Campus — BYOD:</strong> "We\'ll deploy Wi-Fi 6 access points in every classroom and common area, with coverage testing to verify signal strength. Staff connects to a WPA3-Enterprise SSID authenticated via RADIUS/AD. Students get a separate guest SSID on VLAN 50 with bandwidth limits and content filtering."',
        '🎤 <em>"We\'ll deploy <strong>Wi-Fi 6 access points</strong> throughout the facility with coverage testing to verify signal strength in all areas. Employees connect to a <strong>WPA3-Enterprise SSID</strong> authenticated via RADIUS/Active Directory. Guests get a separate SSID on its own <strong>VLAN</strong> with bandwidth limits and content filtering."</em>'
    ),
    # NAT
    (
        '<strong>🏠 Small Business — 30 devices, 1 public IP:</strong> "The router will use PAT (a form of NAT) so all 30 internal devices on our 192.168.1.0/24 network share a single public IP address from the ISP. This conserves IPv4 addresses and provides a layer of security by hiding our internal addressing scheme."',
        '🎤 <em>"The router will use <strong>PAT</strong> (a form of NAT) so all internal devices on our private <strong>[192.168.x.x / 10.x.x.x]</strong> network share a single public IP from the ISP. This conserves IPv4 addresses and adds a layer of security by hiding <strong>[company]</strong>\'s internal addressing scheme from the internet."</em>'
    ),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"OK Replaced scenario")
    else:
        print(f"MISS: {old[:60]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! All scenarios updated to plug-and-play templates.")
