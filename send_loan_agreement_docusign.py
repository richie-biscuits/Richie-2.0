#!/opt/homebrew/bin/python3
"""Send AMPPS-Polynize Loan Agreement via DocuSign using stored token."""
import json, os, base64, requests
import docusign_esign
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Document, Signer, Tabs, SignHere, Recipients, DateSigned

CREDS_PATH = os.path.expanduser("~/.config/richie-credentials/docusign-creds.json")
TOKEN_PATH = os.path.expanduser("~/.config/richie-credentials/docusign_token.json")
PDF_PATH = "/Users/openclaw_admin/.openclaw/media/inbound/AMPPS_Polynize_Loan_Agreement---7eec9297-45db-444e-a000-29c17af7726d.pdf"

with open(CREDS_PATH) as f:
    creds = json.load(f)

with open(TOKEN_PATH) as f:
    token_data = json.load(f)

access_token = token_data["access_token"]
print("✅ Using stored DocuSign token")

# Set up API client
api_client = ApiClient()
api_client.set_base_path("https://demo.docusign.net/restapi")

# Set auth header
api_client.set_default_header("Authorization", f"Bearer {access_token}")

# Use account ID from credentials
account_id = creds["apiAccountId"]
print(f"✅ Using account: {creds['accountEmail']} ({account_id})")

# Read PDF
with open(PDF_PATH, "rb") as f:
    pdf_b64 = base64.b64encode(f.read()).decode("ascii")

doc = Document(
    document_base64=pdf_b64,
    name="AMPPS_Polynize_Loan_Agreement.pdf",
    file_extension="pdf",
    document_id="1"
)

# Signer 1: Shourov Bhattacharya (Polynize) - signs first
shourov = Signer(
    email="shourov@polynize.io",
    name="Shourov Bhattacharya",
    recipient_id="1",
    routing_order="1"
)
shourov.tabs = Tabs(
    sign_here_tabs=[
        SignHere(
            document_id="1",
            page_number="1",
            recipient_id="1",
            anchor_string="Shourov Bhattacharya",
            anchor_units="pixels",
            anchor_y_offset="30",
            anchor_x_offset="150"
        )
    ],
    date_signed_tabs=[
        DateSigned(
            document_id="1",
            page_number="1",
            recipient_id="1",
            anchor_string="Shourov Bhattacharya",
            anchor_units="pixels",
            anchor_y_offset="30",
            anchor_x_offset="350"
        )
    ]
)

# Signer 2: Avik Mukerjee (AMPPS) - signs second
avik = Signer(
    email="avik.mukerjee@ampps.io",
    name="Avik Mukerjee",
    recipient_id="2",
    routing_order="2"
)
avik.tabs = Tabs(
    sign_here_tabs=[
        SignHere(
            document_id="1",
            page_number="1",
            recipient_id="2",
            anchor_string="Avik Mukerjee",
            anchor_units="pixels",
            anchor_y_offset="30",
            anchor_x_offset="150"
        )
    ],
    date_signed_tabs=[
        DateSigned(
            document_id="1",
            page_number="1",
            recipient_id="2",
            anchor_string="Avik Mukerjee",
            anchor_units="pixels",
            anchor_y_offset="30",
            anchor_x_offset="350"
        )
    ]
)

envelope = EnvelopeDefinition(
    email_subject="Please sign: Loan Agreement — AMPPS & Polynize Pty Ltd ($50,000 Bridge Loan)",
    email_blurb="This is the formal loan agreement for the A$50,000 bridge loan advanced on 1 April 2026.\n\nPlease review and sign. Shourov will sign first as Director of Polynize Pty Ltd, then it will be sent to Avik for signature as Director of AMPPS.\n\nKey terms:\n• Interest-free for 12 months\n• 4% p.a. simple interest thereafter\n• Unsecured\n• No fixed maturity date — repayable at Polynize's discretion",
    documents=[doc],
    recipients=Recipients(signers=[shourov, avik]),
    status="sent"
)

envelopes_api = EnvelopesApi(api_client)
result = envelopes_api.create_envelope(account_id, envelope_definition=envelope)
print(f"\n✅ Envelope sent successfully!")
print(f"Envelope ID: {result.envelope_id}")
print(f"Status: {result.status}")
print(f"\nSigning order:")
print(f"  1. Shourov Bhattacharya (shourov@polynize.io) — Director, Polynize Pty Ltd")
print(f"  2. Avik Mukerjee (avik.mukerjee@ampps.io) — Director, AMPPS")
