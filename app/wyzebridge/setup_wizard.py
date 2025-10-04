"""
Interactive Setup Wizard for Wyze Bridge.

This module provides an interactive CLI and web-based setup wizard to guide users
through the configuration process with direct links to Wyze API credential generation.
"""

import sys
from typing import Optional, Dict, Tuple
from wyzebridge.logging import logger


class SetupWizard:
    """Interactive setup wizard for Wyze Bridge configuration."""

    WYZE_API_URL = "https://developer-api-console.wyze.com/#/apikey/view"
    
    def __init__(self):
        """Initialize the setup wizard."""
        self.credentials: Dict[str, str] = {
            "email": "",
            "password": "",
            "api_id": "",
            "api_key": ""
        }

    def print_banner(self):
        """Print welcome banner."""
        print("\n" + "="*70)
        print("   🎬 Wyze Bridge - Interactive Setup Wizard")
        print("="*70)
        print("\nWelcome! This wizard will guide you through setting up your Wyze Bridge.")
        print("You'll need 4 pieces of information:\n")
        print("  1. Wyze account email")
        print("  2. Wyze account password")
        print("  3. Wyze API ID")
        print("  4. Wyze API Key")
        print("\n" + "="*70 + "\n")

    def print_api_instructions(self):
        """Print instructions for getting API credentials."""
        print("\n" + "-"*70)
        print("📋 How to Get Your API Credentials:")
        print("-"*70)
        print("\n1. Visit the Wyze Developer Portal:")
        print(f"   {self.WYZE_API_URL}")
        print("\n2. Sign in with your Wyze account (or create a developer account)")
        print("\n3. Click 'Create API Key' or view existing keys")
        print("\n4. You'll receive:")
        print("   - API ID (36 characters, format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)")
        print("   - API Key (60 characters, alphanumeric)")
        print("\n5. Copy both values - you'll need them in the next steps")
        print("\n" + "-"*70 + "\n")

    def get_input(self, prompt: str, validator=None, secret: bool = False) -> str:
        """
        Get user input with optional validation.

        Args:
            prompt: Input prompt message
            validator: Optional validation function
            secret: Whether to hide input (for passwords)

        Returns:
            Validated user input
        """
        while True:
            if secret:
                import getpass
                value = getpass.getpass(prompt)
            else:
                value = input(prompt).strip()
            
            if not value:
                print("❌ This field cannot be empty. Please try again.")
                continue
            
            if validator:
                is_valid, message = validator(value)
                if not is_valid:
                    print(f"❌ {message}")
                    continue
            
            return value

    def validate_email(self, email: str) -> Tuple[bool, str]:
        """Validate email format."""
        if "@" not in email or "." not in email:
            return False, "Invalid email format. Please enter a valid email address."
        return True, ""

    def validate_api_id(self, api_id: str) -> Tuple[bool, str]:
        """Validate API ID format."""
        # API ID should be 36 characters (UUID format)
        if len(api_id) != 36:
            return False, f"API ID should be 36 characters long (got {len(api_id)})"
        if api_id.count("-") != 4:
            return False, "API ID should be in UUID format (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)"
        return True, ""

    def validate_api_key(self, api_key: str) -> Tuple[bool, str]:
        """Validate API Key format."""
        # API Key should be 60 characters
        if len(api_key) != 60:
            return False, f"API Key should be 60 characters long (got {len(api_key)})"
        if not api_key.isalnum():
            return False, "API Key should only contain letters and numbers"
        return True, ""

    def collect_credentials(self):
        """Collect all credentials from user."""
        print("\n📧 Step 1: Wyze Account Email")
        print("-"*70)
        self.credentials["email"] = self.get_input(
            "Enter your Wyze account email: ",
            validator=self.validate_email
        )
        print("✅ Email accepted\n")

        print("🔐 Step 2: Wyze Account Password")
        print("-"*70)
        self.credentials["password"] = self.get_input(
            "Enter your Wyze account password: ",
            secret=True
        )
        print("✅ Password accepted\n")

        # Show API instructions before asking for API credentials
        self.print_api_instructions()
        
        input("Press Enter when you're ready to continue with API credentials...")

        print("\n🔑 Step 3: API ID")
        print("-"*70)
        print("This is the 36-character UUID from the Wyze Developer Portal")
        self.credentials["api_id"] = self.get_input(
            "Enter your API ID: ",
            validator=self.validate_api_id
        )
        print("✅ API ID accepted\n")

        print("🗝️  Step 4: API Key")
        print("-"*70)
        print("This is the 60-character alphanumeric key from the Wyze Developer Portal")
        self.credentials["api_key"] = self.get_input(
            "Enter your API Key: ",
            validator=self.validate_api_key
        )
        print("✅ API Key accepted\n")

    def display_summary(self):
        """Display configuration summary."""
        print("\n" + "="*70)
        print("📋 Configuration Summary")
        print("="*70)
        print(f"\n✉️  Email:   {self.credentials['email']}")
        print(f"🔐 Password: {'*' * len(self.credentials['password'])}")
        print(f"🔑 API ID:   {self.credentials['api_id'][:8]}...{self.credentials['api_id'][-8:]}")
        print(f"🗝️  API Key:  {self.credentials['api_key'][:10]}...{self.credentials['api_key'][-10:]}")
        print("\n" + "="*70 + "\n")

    def confirm_credentials(self) -> bool:
        """Ask user to confirm credentials."""
        response = input("Are these credentials correct? (yes/no): ").lower().strip()
        return response in ["yes", "y"]

    def save_to_env(self, env_file: str = ".env") -> bool:
        """
        Save credentials to .env file.

        Args:
            env_file: Path to .env file

        Returns:
            True if saved successfully
        """
        try:
            # Read existing .env if it exists
            existing_content = ""
            try:
                with open(env_file, "r") as f:
                    existing_content = f.read()
            except FileNotFoundError:
                pass

            # Update or add credentials
            lines = existing_content.split("\n") if existing_content else []
            cred_keys = {
                "WYZE_EMAIL": self.credentials["email"],
                "WYZE_PASSWORD": self.credentials["password"],
                "API_ID": self.credentials["api_id"],
                "API_KEY": self.credentials["api_key"]
            }

            # Update existing keys or add new ones
            updated_lines = []
            keys_added = set()

            for line in lines:
                key_updated = False
                for key, value in cred_keys.items():
                    if line.startswith(f"{key}="):
                        updated_lines.append(f"{key}={value}")
                        keys_added.add(key)
                        key_updated = True
                        break
                if not key_updated:
                    updated_lines.append(line)

            # Add any missing keys
            for key, value in cred_keys.items():
                if key not in keys_added:
                    updated_lines.append(f"{key}={value}")

            # Write back to file
            with open(env_file, "w") as f:
                f.write("\n".join(updated_lines))

            logger.info(f"[SETUP] Credentials saved to {env_file}")
            return True

        except Exception as e:
            logger.error(f"[SETUP] Failed to save credentials: {e}")
            return False

    def run(self) -> Optional[Dict[str, str]]:
        """
        Run the interactive setup wizard.

        Returns:
            Dictionary of credentials if successful, None otherwise
        """
        try:
            self.print_banner()
            
            while True:
                self.collect_credentials()
                self.display_summary()
                
                if self.confirm_credentials():
                    print("\n✅ Credentials confirmed!")
                    return self.credentials
                else:
                    print("\n🔄 Let's try again...\n")
                    self.credentials = {k: "" for k in self.credentials}

        except KeyboardInterrupt:
            print("\n\n❌ Setup cancelled by user.")
            return None
        except Exception as e:
            logger.error(f"[SETUP] Wizard error: {e}")
            return None

    def print_next_steps(self, hostname: str = "localhost"):
        """Print next steps after successful setup."""
        print("\n" + "="*70)
        print("🎉 Setup Complete!")
        print("="*70)
        print("\n📝 Next Steps:\n")
        print("1. Start the Wyze Bridge:")
        print("   docker-compose up -d")
        print("\n2. Access the Web UI:")
        print(f"   http://{hostname}:5000")
        print("\n3. Your RTSP streams will be available at:")
        print(f"   rtsp://{hostname}:8554/[camera-name]")
        print("\n4. Check the logs:")
        print("   docker-compose logs -f wyze-bridge")
        print("\n" + "="*70 + "\n")


def run_setup_wizard() -> Optional[Dict[str, str]]:
    """
    Run the interactive setup wizard.

    Returns:
        Dictionary of credentials if successful, None otherwise
    """
    wizard = SetupWizard()
    return wizard.run()


if __name__ == "__main__":
    # Allow running the wizard standalone
    wizard = SetupWizard()
    credentials = wizard.run()
    
    if credentials:
        # Try to save to .env
        if wizard.save_to_env():
            print("\n✅ Credentials saved to .env file")
            wizard.print_next_steps()
        else:
            print("\n❌ Failed to save credentials")
            print("Please manually add these to your .env file:")
            for key, value in credentials.items():
                print(f"{key.upper()}={value}")
    else:
        sys.exit(1)
