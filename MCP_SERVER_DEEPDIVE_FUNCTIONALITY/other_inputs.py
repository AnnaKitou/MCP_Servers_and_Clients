from pathlib import Path
from mcp.server.fastmcp import FastMCP 
from pydantic import BaseModel, Field
from typing import List

mcp = FastMCP("Other Inputs")
LOGS_FILE = Path(__file__).resolve().with_name("log.txt")

class Person(BaseModel):
 first_name: str = Field(..., description="The person's first name")
 last_name: str = Field(..., description="The person's last name") 
 years_of_experience: int = Field(..., description="The person's years of experience in their field")
 previous_addresses: List[str] = Field(default_factory=list, description="A list of the person's previous addresses")

 

@mcp.tool()
def add_person_to_member_database(person: Person) -> str:
    """
    Log the person's information to the member database.
    Args:
      person(Person): An instance of the Person class containing the following personal details:
        - first_name (str): The person's first name.
        - last_name (str): The person's last name.
        - years_of_experience (int): The person's years of experience in their field.
        - previous_addresses (List[str]): A list of the person's previous addresses.
    Returns:
      str: A confirmation message indicating that the person's information has been logged.
    """
    with open(LOGS_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"First Name: {person.first_name}\n")
        log_file.write(f"Last Name: {person.last_name}\n")
        log_file.write(f"Years of Experience: {person.years_of_experience}\n")
        log_file.write("Previous Addresses:\n")
        for idx, address in enumerate(person.previous_addresses, 1):
            log_file.write(f" {idx}. {address}\n")
        log_file.write("\n")  # Add a newline for better readability        
        return "Data logged successfully."
    
    if __name__ == "__main__":
        mcp.run()