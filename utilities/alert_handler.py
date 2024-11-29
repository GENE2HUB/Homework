import os
import logging
import datetime
import allure
import traceback
from typing import Dict, Any, Optional


class AlertHandler:
    """
    Centralized alert handling and logging utility for test automation.

    Key Responsibilities:
    - Configure logging mechanism
    - Track and categorize alerts
    - Capture screenshots on failures
    - Log exceptions and test events
    """

    def __init__(self, log_dir='logs'):
        """
        Initialize AlertHandler with logging configuration.

        Args:
            log_dir (str): Directory to store log files. Defaults to 'logs'.
        """
        # Create logs directory if it doesn't exist
        self.log_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.log_dir, exist_ok=True)

        # Configure logging
        self.logger = self._configure_logging()

        # Initialize alert tracking dictionary
        self.alerts = {
            'warnings': [],  # Non-critical but noteworthy events
            'errors': [],  # Significant issues affecting test execution
            'critical_alerts': []  # Severe problems requiring immediate attention
        }

    def _configure_logging(self):
        """
        Set up logging configuration with timestamped log files.

        Returns:
            logging.Logger: Configured logger instance
        """
        # Generate unique timestamp for log file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.log_dir, f'test_run_{timestamp}.log')

        # Configure logging with file and console handlers
        logging.basicConfig(
            level=logging.INFO,  # Log all info, warning, and error messages
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),  # Save logs to file
                logging.StreamHandler()  # Print logs to console
            ]
        )
        return logging.getLogger('flight_automation_logger')

    def add_alert(self, alert_type: str, message: str, details: Optional[Dict] = None):
        """
        Record an alert with specified type, message, and optional details.

        Args:
            alert_type (str): Type of alert ('warnings', 'errors', 'critical_alerts')
            message (str): Description of the alert
            details (dict, optional): Additional context about the alert
        """
        # Create alert entry with timestamp and details
        alert_entry = {
            'timestamp': datetime.datetime.now(),
            'message': message,
            'details': details or {}  # Use empty dict if no details provided
        }

        # Store alert in appropriate category
        self.alerts[alert_type].append(alert_entry)

        # Log based on alert severity
        if alert_type == 'warnings':
            self.logger.warning(message)
        elif alert_type == 'errors':
            self.logger.error(message)
        elif alert_type == 'critical_alerts':
            self.logger.critical(message)

    def capture_screenshot(self, driver, test_name):
        """
        Capture and attach a screenshot for debugging.

        Args:
            driver: Selenium WebDriver instance
            test_name (str): Name of the test for screenshot identification
        """
        # Create screenshots directory
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)

        # Generate unique screenshot filename
        screenshot_path = os.path.join(
            screenshot_dir,
            f'{test_name}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        )

        # Capture screenshot
        driver.save_screenshot(screenshot_path)

        # Attach to Allure report for easy access
        allure.attach.file(
            screenshot_path,
            name=f'{test_name}_screenshot',
            attachment_type=allure.attachment_type.PNG
        )

    def log_exception(self, exception, test_name):
        """
        Detailed logging of exceptions for troubleshooting.

        Args:
            exception (Exception): The exception that occurred
            test_name (str): Name of the test where exception happened
        """
        # Log exception details
        self.logger.error(f"Exception in {test_name}")
        self.logger.error(str(exception))
        self.logger.error(traceback.format_exc())  # Full stack trace

    def get_alert_summary(self):
        """
        Generate a summary of alerts by type.

        Returns:
            dict: Count of alerts for each category
        """
        summary = {}
        for alert_type in ['critical_alerts', 'errors', 'warnings']:
            summary[alert_type] = len(self.alerts[alert_type])
        return summary