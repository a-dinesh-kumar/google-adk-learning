"""
Test script to see state access directly.
Run with: python test_state.py
"""

import os
from dotenv import load_dotenv

# 1. Load environment variables BEFORE importing the agent code
load_dotenv()

import asyncio  
from agent import root_agent  
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def main():
    session_service = InMemorySessionService()
    
    # Create the session track
    session = await session_service.create_session(
        app_name="name_extractor_app",
        user_id="test_user",
        session_id="test_session"
    )

    runner = Runner(
        agent=root_agent,
        app_name="name_extractor_app",
        session_service=session_service
    )

    # --- TURN 1: Provide Name ---
    user_message = Content(parts=[Part(text="Hi, my name is Alex Johnson")])

    print("=== Running agent ===")
    result = runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=user_message
    )

    for event in result:
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"\nAgent response: {event.content.parts[0].text.strip()}")

    # Access state programmatically by retrieving the updated session record from the store
    updated_session = await session_service.get_session(
        app_name="name_extractor_app", 
        user_id="test_user", 
        session_id="test_session"
    )

    print(f"\n=== State after execution ===")
    print(f"Full state: {updated_session.state}")
    print(f"Extracted name: {updated_session.state.get('user_name')}")

    # FIX: Evaluate using the fresh updated_session object, not the stale initial session variable
    if updated_session.state.get("user_name"):
        print("Name was successfully extracted and stored!")
    else:
        print("Name extraction failed")

    # --- TURN 2: Verify Persistence ---
    print("\n=== Simulating second turn ===")
    result2 = runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=Content(parts=[Part(text="What's my name?")])
    )

    for event in result2:
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Agent response: {event.content.parts[0].text.strip()}")

    # Fetch fresh session state again to check state boundaries across turns
    final_session = await session_service.get_session(
        app_name="name_extractor_app", 
        user_id="test_user", 
        session_id="test_session"
    )
    print(f"\nState still contains: {final_session.state.get('user_name')}")
    print("State persists across turns!")

if __name__ == "__main__":
    asyncio.run(main())
