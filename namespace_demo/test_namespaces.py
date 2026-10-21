"""
Test state namespaces to see persistence differences.
Run with: python test_namespaces.py
"""

import os
from dotenv import load_dotenv

# 1. Load environment variables before importing ADK agent code
load_dotenv()

import asyncio
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def main():
    # Setup session service
    session_service = InMemorySessionService()
    
    # CORRECTED: Await the asynchronous session creation coroutine
    session = await session_service.create_session(
        app_name="namespace_demo_app",
        user_id="user1",
        session_id="session1"
    )

    runner = Runner(
        agent=root_agent,
        app_name="namespace_demo_app",
        session_service=session_service
    )

    # Set all four namespace types
    print("=== Setting state in all namespaces ===")
    session.state["app:name"] = "Namespace Demo"
    session.state["app:version"] = "2.0"
    session.state["user:theme"] = "dark"
    session.state["topic"] = "state management"
    session.state["temp:step"] = "initialization"

    print(f"State before run: {session.state}\n")

    # Run agent (Turn 1)
    print("=== Running agent (Turn 1) ===")
    result = runner.run(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Show me the namespace values")])
    )

    # Show response
    for event in result:
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Agent response:\n{event.content.parts[0].text}\n")

    # CORRECTED: Refresh the session handle from memory to observe framework transformations
    updated_session1 = await session_service.get_session(
        app_name="namespace_demo_app", 
        user_id="user1", 
        session_id="session1"
    )

    # Check state after turn
    print("=== State after Turn 1 ===")
    print(f"Full state: {updated_session1.state}")
    print(f"temp:step: {updated_session1.state.get('temp:step')}")      # Temp namespace -> Cleared automatically
    print(f"topic: {updated_session1.state.get('topic')}")              # Default namespace -> Persists
    print(f"user:theme: {updated_session1.state.get('user:theme')}")      # User namespace -> Persists
    print(f"app:version: {updated_session1.state.get('app:version')}")  # App namespace -> Persists

    # Simulating Turn 2 (same session)
    print("\n=== Simulating Turn 2 (same session) ===")
    result2 = runner.run(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Check state again")])
    )

    for event in result2:
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Agent response:\n{event.content.parts[0].text}\n")

    # CORRECTED: Fetch fresh session state tracking for Turn 2 evaluation
    updated_session1_turn2 = await session_service.get_session(
        app_name="namespace_demo_app", 
        user_id="user1", 
        session_id="session1"
    )

    print("=== State after Turn 2 ===")
    print(f"Full state: {updated_session1_turn2.state}")
    print(f"temp:step: {updated_session1_turn2.state.get('temp:step')}")
    print(f"topic: {updated_session1_turn2.state.get('topic')}")
    print(f"user:theme: {updated_session1_turn2.state.get('user:theme')}")

    # Simulate cross-session boundary check (New session, same user profile)
    print("\n=== Simulating NEW Session (session2) ===")
    session2 = await session_service.create_session(
        app_name="namespace_demo_app",
        user_id="user1",      # Same user
        session_id="session2" # Different session container
    )

    print(f"New session state: {session2.state}")
    print(f"topic: {session2.state.get('topic')}")              # Should be None (Session-scoped)
    print(f"user:theme: {session2.state.get('user:theme')}")      # Should persist (User-scoped)
    print(f"app:version: {session2.state.get('app:version')}")  # Should persist (App-scoped)

if __name__ == "__main__":
    # Boot the execution pipeline loop
    asyncio.run(main())
