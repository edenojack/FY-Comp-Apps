# Import relevant modules
import Library.BooleanMath as BooleanMath
import Library.Testing as Testing

###Input pair cases
TrueCases = {
    "A": True,
    "B": True,
}

FalseCases = {
    "A": False,
    "B": False,
}

MixedCases = {
    "A": False,
    "B": True,
}

### Larger input cases
L_TrueCases = {
    "A": True,
    "B": True,
    "C": True,
    "D": True,
}

L_FalseCases = {
    "A": False,
    "B": False,
    "C": False,
    "D": False,
}

L_MixedCases = {
    "A": False,
    "B": True,
    "C": False,
    "D": True,
}

##Test case; Requires some kind of input UI to operate, need to be able to say "Input 1/2/3/4, please run it, please change X."
# This should be handled via a small UI window that displays the inputs and outputs form the given equations.

##Testing individual Logic Gate outputs

#OrGate
OR_Tests = [
    Testing.Test_Expected(True, BooleanMath.OR_Gate, MixedCases),
    Testing.Test_Expected(True, BooleanMath.OR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.OR_Gate, FalseCases),
    Testing.Test_Expected(True, BooleanMath.OR_Gate, MixedCases),
    Testing.Test_Expected(True, BooleanMath.OR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.OR_Gate, FalseCases),
]
OR_Tests_String = {
    "Mixed inputs":             OR_Tests[0],
    "True only inputs":         OR_Tests[1],
    "False only inputs":        OR_Tests[2],
    "Multi Mixed inputs":       OR_Tests[3],
    "Multi True only inputs":   OR_Tests[4],
    "Multi False only inputs":  OR_Tests[5],
}
print("OR_Gate")
OR_Tests_Results = Testing.Test_Multiple(OR_Tests)
print("Cases being tested:", len(OR_Tests), "| Succcess rate is;", OR_Tests_Results)
for Key in OR_Tests_String:
        Value = OR_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

#ANDGate
AND_Tests = [
    Testing.Test_Expected(False, BooleanMath.AND_Gate, MixedCases),
    Testing.Test_Expected(True, BooleanMath.AND_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.AND_Gate, FalseCases),
    Testing.Test_Expected(False, BooleanMath.AND_Gate, MixedCases),
    Testing.Test_Expected(True, BooleanMath.AND_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.AND_Gate, FalseCases),
]

AND_Tests_String = {
    "Mixed inputs":             AND_Tests[0],
    "True only inputs":         AND_Tests[1],
    "False only inputs":        AND_Tests[2],
    "Multi Mixed inputs":       AND_Tests[3],
    "Multi True only inputs":   AND_Tests[4],
    "Multi False only inputs":  AND_Tests[5],
}
print("AND_Gate")
AND_Tests_Results = Testing.Test_Multiple(AND_Tests)
print("Cases being tested:", len(AND_Tests), "| Succcess rate is;", AND_Tests_Results)
for Key in AND_Tests_String:
        Value = AND_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

#NANDGate
NAND_Tests = [
    Testing.Test_Expected(True, BooleanMath.NAND_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.NAND_Gate, TrueCases),
    Testing.Test_Expected(True, BooleanMath.NAND_Gate, FalseCases),
    Testing.Test_Expected(True, BooleanMath.NAND_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.NAND_Gate, TrueCases),
    Testing.Test_Expected(True, BooleanMath.NAND_Gate, FalseCases),
]

NAND_Tests_String = {
    "Mixed inputs":             NAND_Tests[0],
    "True only inputs":         NAND_Tests[1],
    "False only inputs":        NAND_Tests[2],
    "Multi Mixed inputs":       NAND_Tests[3],
    "Multi True only inputs":   NAND_Tests[4],
    "Multi False only inputs":  NAND_Tests[5],
}
print("NAND_Gate")
NAND_Tests_Results = Testing.Test_Multiple(NAND_Tests)
print("Cases being tested:", len(NAND_Tests), "| Succcess rate is;", NAND_Tests_Results)
for Key in NAND_Tests_String:
        Value = NAND_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

#XORGate
XOR_Tests = [
    Testing.Test_Expected(True, BooleanMath.XOR_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, FalseCases),
    Testing.Test_Expected(True, BooleanMath.XOR_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, FalseCases),
]

XOR_Tests_String = {
    "Mixed inputs":             XOR_Tests[0],
    "True only inputs":         XOR_Tests[1],
    "False only inputs":        XOR_Tests[2],
    "Multi Mixed inputs":       XOR_Tests[3],
    "Multi True only inputs":   XOR_Tests[4],
    "Multi False only inputs":  XOR_Tests[5],
}
print("XOR_Gate")
XOR_Tests_Results = Testing.Test_Multiple(XOR_Tests)
print("Cases being tested:", len(XOR_Tests), "| Succcess rate is;", XOR_Tests_Results)
for Key in XOR_Tests_String:
        Value = XOR_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

#XORGate
NOR_Tests = [
    Testing.Test_Expected(True, BooleanMath.XOR_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, FalseCases),
    Testing.Test_Expected(True, BooleanMath.XOR_Gate, MixedCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, TrueCases),
    Testing.Test_Expected(False, BooleanMath.XOR_Gate, FalseCases),
]

NOR_Tests_String = {
    "Mixed inputs":             NOR_Tests[0],
    "True only inputs":         NOR_Tests[1],
    "False only inputs":        NOR_Tests[2],
    "Multi Mixed inputs":       NOR_Tests[3],
    "Multi True only inputs":   NOR_Tests[4],
    "Multi False only inputs":  NOR_Tests[5],
}
print("NOR_Gate")
NOR_Tests_Results = Testing.Test_Multiple(NOR_Tests)
print("Cases being tested:", len(NOR_Tests), "| Succcess rate is;", NOR_Tests_Results)
for Key in NOR_Tests_String:
        Value = NOR_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

##Testing Sequential Logic Gate outputs
# Testing an expected outcome across multiple gates


 #Gates, F = (A.B)+(B.C.D)+A'
    # Expected Positive F outcomes;
    # If both A and B are positive, True
    # If B and C and D are positive, True
    # If A is not positive, True
def Test_Sequential(A, B, C, D):
    Inputs = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
    }
    FirstGates = {
        "A.B": BooleanMath.AND_Gate(
            {   "A": A,
                "B": B}
        ),
        "B.C.D": BooleanMath.AND_Gate(
            {   "C": C,
                "B": B,
                "D": D}
        ),
        "A'": BooleanMath.NAND_Gate({"A": A})
    }

    SecondGate = BooleanMath.OR_Gate(FirstGates)
    return SecondGate


#XORGate
Sequence_Tests = [
    Testing.Test_Expected(True,     Test_Sequential, True, True, True, True),
    Testing.Test_Expected(False,    Test_Sequential, True, False, True, True),
    Testing.Test_Expected(False,    Test_Sequential, True, False, False, True),
    Testing.Test_Expected(True,     Test_Sequential, False, True, True, True),
    Testing.Test_Expected(True,    Test_Sequential, True, True, True, False),
    Testing.Test_Expected(True,    Test_Sequential, False, False, False, False),
]

Sequence_Tests_String = {
    "All True":         Sequence_Tests[0],
    "B False":          Sequence_Tests[1],
    "B/C False":        Sequence_Tests[2],
    "A False":          Sequence_Tests[3],
    "D False":          Sequence_Tests[4],
    "All False":        Sequence_Tests[5],
}
print("Sequence_Tests")
Sequence_Tests_Results = Testing.Test_Multiple(Sequence_Tests)
print("Cases being tested:", len(Sequence_Tests), "| Succcess rate is;", Sequence_Tests_Results)
for Key in Sequence_Tests_String:
        Value = Sequence_Tests_String[Key]
        print("Test Case is;", Key, "Test Result is", Value and "Pass" or "Fail")

TotalTestBrackets = [Sequence_Tests_Results, NOR_Tests_Results, AND_Tests_Results, XOR_Tests_Results, NAND_Tests_Results, OR_Tests_Results]

print("\nTest Report\n")
print("Final Test case results pass rate:", Testing.Test_Multiple(TotalTestBrackets)/100,"% of", len(TotalTestBrackets)*6, "tests")
print("OR_Gate")
print("Cases tested:", len(OR_Tests), "| Succcess rate is;", OR_Tests_Results)
print("AND_Gate")
print("Cases tested:", len(AND_Tests), "| Succcess rate is;", AND_Tests_Results)
print("NAND_Gate")
print("Cases tested:", len(NAND_Tests), "| Succcess rate is;", NAND_Tests_Results)
print("XOR_Gate")
print("Cases tested:", len(XOR_Tests), "| Succcess rate is;", XOR_Tests_Results)
print("NOR_Gate")
print("Cases tested:", len(NOR_Tests), "| Succcess rate is;", NOR_Tests_Results)
print("Sequence_Tests")
print("Cases tested:", len(Sequence_Tests), "| Succcess rate is;", Sequence_Tests_Results)