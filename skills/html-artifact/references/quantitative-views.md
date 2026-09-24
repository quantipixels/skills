# Quantitative views

Use a table for exact lookup; use a plot when pattern, trend, spread or outliers matter. Preserve units, population, source revision and material uncertainty. Do not invent values to fill a chart.

Observable Plot is a useful focused capability, not a mandatory dependency. Reuse an installed version and current official API; pin a new runtime when selected. Keep it out of artifacts with no quantitative relationship. Apply the delivery/privacy policy before loading any remote module.

## Small starting recipe

The following is an authoring specimen for supplied tabular data, not a bundled renderer or measured result. `rows` must be validated by the source owner. Native SVG or another existing chart system may be cheaper for one small view.

```js
const chart = Plot.plot({
  ariaLabel: "Elapsed time by observed batch size",
  x: {label: "Batch size (items)"},
  y: {label: "Elapsed time (ms)", grid: true},
  marks: [
    Plot.line(rows, {x: "items", y: "milliseconds"}),
    Plot.dot(rows, {x: "items", y: "milliseconds", tip: true})
  ]
});
container.replaceChildren(chart);
```

Start with `Plot.barY` for category comparisons, `Plot.dot` for paired values or scatter, and a documented bin transform for distributions. Confirm transformation semantics; line interpolation, binning and normalisation can change interpretation. Preserve the source table. Do not rely on hover-only tips as the accessible or touch reading path.

For a what-if view, keep measured data and calculated outputs visually distinct. Use a domain-owned calculation, labelled native inputs, visible units and reset-to-baseline; test one known result and a rejected input. No persistence or feedback export is implied. Do not create a generic model-control asset merely to replace native inputs.

Primary references: [Plot](https://observablehq.com/plot/), [marks](https://observablehq.com/plot/marks/), [pointer](https://observablehq.com/plot/interactions/pointer). Check selected-version support for proposed interactions before making them part of acceptance.
