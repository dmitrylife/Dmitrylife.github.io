---
layout: note
title: Kinematic connection to GR
order: 7
permalink: /notes/07_kinematic_connection_to_gr/
---

# From definition to evolution: the kinematics of Ψ(z)

Interpretational layer · no new models · direct consequence of definitions

This note shows that the evolution of Ψ(z) follows directly from its definition and the standard kinematics of FLRW cosmology. No additional assumptions are introduced.

---

## 1. Starting point

Define the diagnostic quantity:

$$
\Psi(z) = \frac{H(z)}{H_\Lambda(z)} - 1,
$$

where:

- \(H(z)\) is the observed expansion rate,
- \(H_\Lambda(z)\) is the reference ΛCDM expansion history.

This definition is purely operational.

---

## 2. Change of variable

It is convenient to use:

$$
x = \ln a,
$$

so that derivatives describe evolution per logarithmic change of scale factor.

---

## 3. Evolution of H

In FLRW cosmology, the deceleration parameter is:

$$
q = -\frac{\ddot a}{a H^2}.
$$

From this definition, one obtains the identity:

$$
\frac{dH}{dx} = -H(1+q).
$$

The same holds for the reference model:

$$
\frac{dH_\Lambda}{dx} = -H_\Lambda(1+q_\Lambda).
$$

These relations are purely kinematical and follow from GR.

---

## 4. Differentiating Ψ

Differentiate:

$$
\Psi = \frac{H}{H_\Lambda} - 1.
$$

Using the quotient rule:

$$
\frac{d\Psi}{dx}
= \frac{1}{H_\Lambda}\frac{dH}{dx}
- \frac{H}{H_\Lambda^2}\frac{dH_\Lambda}{dx}.
$$

Substitute the expressions from Section 3:

$$
\frac{d\Psi}{dx}
= \frac{-H(1+q)}{H_\Lambda}
- \frac{H}{H_\Lambda^2}\left[-H_\Lambda(1+q_\Lambda)\right].
$$

---

## 5. Simplification

Simplify step by step:

$$
\frac{d\Psi}{dx}
= -\frac{H}{H_\Lambda}(1+q)
+ \frac{H}{H_\Lambda}(1+q_\Lambda).
$$

Factor:

$$
\frac{d\Psi}{dx}
= \frac{H}{H_\Lambda}(q_\Lambda - q).
$$

Using:

$$
\frac{H}{H_\Lambda} = 1+\Psi,
$$

we obtain:

$$
\boxed{
\frac{d\Psi}{dx} = (1+\Psi)(q_\Lambda - q).
}
$$

---

## 6. Interpretation

This equation is not a model.

It is an identity that follows from:

- the definition of Ψ,
- the standard FLRW relations.

It shows that:

- Ψ evolves only if the real and reference deceleration differ,
- Ψ = 0 corresponds to exact agreement with ΛCDM,
- deviations accumulate through differences in \(q\).

---

## 7. Geometric form

Using:

$$
K = -3H,
$$

the same relation can be written as:

$$
\Psi = \frac{K}{K_\Lambda} - 1,
$$

which shows that Ψ measures relative deformation of the background geometry.

---

## 8. Minimal conclusion

The evolution of Ψ(z):

- does not require new physics,
- does not introduce new parameters,
- follows directly from how we compare two expansion histories.

---

## 9. Diagnostic meaning

The equation

$$
\frac{d\Psi}{d\ln a} = (1+\Psi)(q_\Lambda - q)
$$

provides a closed, observable-level description of deviation.

It shifts the question from:

> what causes acceleration?

to:

> how does the observed trajectory differ from the reference one?

---

## 10. Scope

This result:

- is exact at the background level,
- is independent of any interpretation (relaxation, memory, etc.),
- serves as a stable foundation for further conceptual layers.

---

## Conclusion

Ψ(z) is not an assumed field.

It is a derived coordinate whose evolution is fully determined by observable kinematics within standard GR.

No additional structure is required to obtain its dynamics.

