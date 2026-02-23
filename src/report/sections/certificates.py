def certificates(data):
    certs = data["certificates"]

    content = []
    content.append("\n\n\nF. CERTIFICATES")
    content.append("-" * 30)
    content.append("")

    vdm_certs = [
        cert for cert in certs.values() if cert.get("friendly_name") == "vdm"
    ]

    if not vdm_certs:
        content.append("   VDM Certificate Not Found.")
        return "\n".join(content)

    content.append("VDM Certificate(s):")
    if len(vdm_certs) > 1:
        content.append("\n * MULTIPLE VDM CERTIFICATES DETECTED.")

    field_names = [
        "Friendly Name",
        "Serial Number",
        "Issuer",
        "Subject",
        "Subject Alternative Name(s)",
        "Valid From (Not Before)",
        "Valid To (Not After)",
        "Has Private Key",
        "Private Key Exportable",
    ]

    max_width = max(len(key) for key in field_names)

    for i, vdm_cert in enumerate(vdm_certs, start=1):
            content.append(f"\n   #{i}")

            has_private_key = vdm_cert.get("has_private_key")
            private_key_exportable = vdm_cert.get("private_key_exportable")

            if not has_private_key:
                has_private_key_display = "No"
                private_key_exportable_display = "N/A"
            else:
                has_private_key_display = "Yes"
                private_key_exportable_display = (
                    "Yes" if private_key_exportable else "No"
                )

            fields = {
                "Friendly Name": vdm_cert.get("friendly_name"),
                "Serial Number": vdm_cert.get("serial_number"),
                "Issuer": vdm_cert.get("issuer"),
                "Subject": vdm_cert.get("subject"),
                "Subject Alternative Name(s)": vdm_cert.get("subject_alt_name"),
                "Valid From (Not Before)": vdm_cert.get("not_before"),
                "Valid To (Not After)": vdm_cert.get("not_after"),
                "Has Private Key": has_private_key_display,
                "Private Key Exportable": private_key_exportable_display,
            }

            for key, value in fields.items():
                value = value if value is not None else "False"
                
                if key == "Issuer" or key == "Subject":
                    content.append(f"     - {key:<{max_width}} : {value['CN']}")
                    continue

                if key == "Subject Alternative Name(s)":
                    content.append(f"     - {key:<{max_width}} :")

                    if isinstance(value, list):
                        for item in value:
                            content.append(f"         {'':<{max_width}} {item['value']}")
                    else:
                        content.append(f"        {'':<{max_width}}   {value}")
                    continue

                content.append(f"     - {key:<{max_width}} : {value}")
                 
    return "\n".join(content)