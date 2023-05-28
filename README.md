# python_mop
python toolkit for monitor-oriented programming.

## What is MOP?
Monitoring-Oriented Programming (MOP) is a software development and analysis framework that aims to bridge the gap between formal specifications and implementations by combining them. In MOP, runtime monitoring is considered a fundamental principle for building reliable software, automatically synthesized from specified attributes and integrated with the original system through auto-generated monitors to check its dynamic behavior during execution. When a specification is violated or validated at runtime, user-defined actions are triggered, which can be any code: from logging information to runtime recovery.

The main steps of MOP are as follows:

1. Formal specification: Write specifications for the properties and behavior of the system using a formal language, which helps clarify the correctness requirements of the system.

2. Code synthesis: Generate monitors to monitor system behavior according to formal specifications. These monitors are executed with the system at runtime to detect if the system violates or meets specifications.

3. Integration and execution: Integrate the generated monitor with the system, enabling it to inspect the behavior of the system at runtime and trigger predefined actions when specifications are violated or validated.

4. Feedback and adjustment: Based on the results of runtime monitoring, collect feedback information on system behavior, and adjust formal specifications and implementations accordingly to further improve the reliability of the system.

Merit:

1. Clearer specifications: By using formal specifications to write the properties and behavior of the system, MOP helps developers clearly understand the correctness requirements of the system.

2. Higher reliability: The MOP framework improves the reliability of the system by integrating monitors with the system, enabling the detection of specification violations at runtime.

3. Real-time diagnosis and repair: By taking predefined actions based on runtime monitoring results, MOP can diagnose and repair system problems in real time, reducing the loss caused by errors.

4. Validation and tuning: The runtime monitoring results collected by MOP can be used for feedback to adjust formal specifications and implementations to improve system correctness and performance.

Shortcoming:

1. Performance overhead: Runtime monitoring introduces a certain level of performance overhead, which may affect the speed of the system.

2. Implementation complexity: MOP frameworks sometimes increase implementation complexity by requiring developers to be familiar with formal specification languages and to be able to generate monitor code based on specifications.

3. Not suitable for all fields: MOP is mainly for systems that require high reliability, and for some fields or specific application scenarios, MOP may be too complex or not the most efficient method.

## Examples

```python
import mop


@mop.monitor(lambda v: 4 < v < 6, lambda v: 5)
def add0(a, b):
    return a + b


print(add0(1.1, 1.1))


@mop.monitor(int, int)
def add1(a, b):
    return a + b


print(add1(1.1, 1.1))


# 2

@mop.monitor(mop.mrv() == 1, None, 1)
def add2(a, b):
    return a + b


print(add2(1.1, 1.1))
# 1
```